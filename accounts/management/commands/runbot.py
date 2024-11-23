from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from accounts.models import DiscordUser
from notice.models import EmbedMessage
from reminder.models import Schedule, Category
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async

import discord
from discord import app_commands
from discord.ext import tasks

import datetime

from os.path import dirname, basename, isfile, join
from importlib import import_module
import glob

from .bot.commands import print_commands, find_commands


CustomUser = get_user_model()

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

    # Activity
    new_activity = f"スラッシュコマンドのテスト"
    await client.change_presence(activity=discord.Game(new_activity))

    # スラッシュコマンドを同期
    await tree.sync()

    loop.start()


@client.event
async def on_message(message):
    if message.author == client.user:
        # ignore messages that I send to myself
        return

    channel_name = "%s:%s" % (str(message.guild), str(message.channel))

    command = find_commands(message.content)
    if command:
        await command(channel_name, message)
    else:
        pass


@app_commands.default_permissions(administrator=True)
@tree.command(name="sendembed", description="特定の埋め込みメッセージを送信します")
async def send_embed_message(ctx:discord.Interaction, message_key:int):
    description = await sync_to_async(_get_message_description, thread_sensitive=True)(message_key)

    if description == None:
        description = "None"

    embed = discord.Embed(
        color=0x349961,
        description=description,
    )
    await ctx.response.send_message(f"埋め込みメッセージ#{message_key}を送信しました", ephemeral=True)
    await ctx.channel.send(embed=embed)


def _get_message_description(key):
    try:
        message = EmbedMessage.objects.all().get(key=key)
        return message.description
    except:
        return None


@tree.command(name="sendschedule", description="特定のスケジュールを送信します")
@discord.app_commands.describe(
    schedule_id="スケジュールIDはスケジュール詳細ページで確認できます)"
)
async def send_the_schedule(ctx:discord.Interaction, schedule_id:int):
    url = await sync_to_async(_get_schedule_url, thread_sensitive=True)(schedule_id)
    description = await sync_to_async(_get_schedule_description, thread_sensitive=True)(schedule_id)
    if not description:
        description = "None"
    embed = discord.Embed(
        title=(f"スケジュール #{schedule_id}"),
        color=0x349961,
        description=description,
        url=url,
    )
    embed.set_thumbnail(url=ctx.guild.icon.url)
    await ctx.response.send_message(embed=embed)


def _get_schedule_url(schedule_id):
    return "https://aaaaaaaaaaaaaaaaaa.com"


def _get_schedule_description(schedule_id):
    try:
        schedule = Schedule.objects.all().get(pk=schedule_id)
        description = f"`カテゴリー`：{schedule.category.name}\n`教科`：{schedule.subject.name}\n`タイトル`：{schedule.title}\n`詳細`：{schedule.detail}\n`締め切り日`：{schedule.deadline}"
        return description
    except:
        return None


@tree.command(name="active", description="アクティブボタンを表示します")
async def display_button(interaction:discord.Interaction):
    await interaction.response.send_message("アクティブボタンを表示しました", view=ActiveButton(), ephemeral=True)


class ActiveButton(discord.ui.View):
    
    @discord.ui.button(label="Active!", style=discord.ButtonStyle.green, row=4)
    async def pressedButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        reply = await sync_to_async(_associate_user, thread_sensitive=True)(interaction.user.name, interaction.user.id)
        await interaction.response.send_message(reply, ephemeral=True)


def _associate_user(username, discord_id):
    # 新規Discordユーザーならば登録
    try:
        du = DiscordUser.objects.all().get(discord_id=discord_id)
    except:
        du = DiscordUser()
        du.username = username
        du.discord_id = discord_id
        du.save()
    
    # サインアップ済みユーザーならばアクティブ化
    try:
        cu = CustomUser.objects.all().filter(is_active=True).get(discord_id=discord_id)
    except:
        try:
            cu = CustomUser.objects.all().get(discord_id=discord_id)
            cu.is_active = True
            cu.save()
            return "### あなたのアカウントは無事アクティブ化されました。"
        except:
            return "### サインアップはしましたか？"

    # ユーザーネームが変更されたユーザーならば変更
    try:
        dun = DiscordUser.objects.all().get(username=username)
    except:
        dun = DiscordUser.objects.all().get(discord_id=discord_id)
        dun.username = username
        dun.save()
        return "### あなたのDiscordのユーザー名を更新しました。"

    # アクティブ化済みユーザーにはエラーメッセージ
    if cu.is_active:
        return "### あなたのアカウントは既にアクティブ化されています。"


@tasks.loop(seconds=60)
async def loop():
    # botが起動するまで待つ
    await client.wait_until_ready()
    now = datetime.datetime.now().strftime('%H:%M')
    if now == '07:00':
        await sync_to_async(_delete_previous_schedule, thread_sensitive=True)()
        date = datetime.date.today() + datetime.timedelta(days=1)
        category_list = await sync_to_async(_get_category_id_list, thread_sensitive=True)()
        if category_list:
            for i in category_list:
                name = await sync_to_async(_get_category_name, thread_sensitive=True)(i)
                channel_id = await sync_to_async(_get_category_channel_id, thread_sensitive=True)(i)
                channel = client.get_channel(channel_id)
                schedule_list = await sync_to_async(_get_schedule_id_list, thread_sensitive=True)(i, date)
                if schedule_list:
                    await channel.send(f"### 明日（{date.strftime('%m月%d日')}）の{name}は以下の通りです\n@everyone")
                    for j in schedule_list:
                        description = await sync_to_async(_get_schedule_description_alpha, thread_sensitive=True)(j)
                        url = await sync_to_async(_get_schedule_url, thread_sensitive=True)(j)
                        embed = discord.Embed(
                            title=(f"スケジュール #{j}"),
                            color=0x349961,
                            description=description,
                            url=url,
                        )
                        embed.set_thumbnail(url=channel.guild.icon.url)
                        await channel.send(embed=embed)
                else:
                    await channel.send(f"明日（{date.strftime('%m月%d日')}）の{name}はありません")


def _get_category_id_list():
    try:
        categories = Category.objects.all()
        id_list = [category.pk for category in categories]
        return id_list
    except:
        return None


def _get_schedule_id_list(category_id, date):
    try:
        schedules = Schedule.objects.all().filter(deadline=date)
        id_list = []
        for schedule in schedules:
            if schedule.category.pk == category_id:
                id_list.append(schedule.pk)
        return id_list
    except:
        return None


def _get_category_channel_id(category_id):
    try:
        category = Category.objects.get(pk=category_id)
        return int(category.channel_id)
    except:
        return None


def _get_category_name(category_id):
    try:
        category = Category.objects.get(pk=category_id)
        return category.name
    except:
        return "None"


def _get_schedule_description_alpha(schedule_id):
    try:
        schedule = Schedule.objects.all().get(pk=schedule_id)
        description = f"`教科`：{schedule.subject.name}\n`タイトル`：{schedule.title}\n`詳細`：{schedule.detail}"
        return description
    except:
        return None


def _delete_previous_schedule():
    date = datetime.date.today()
    try:
        schedules = Schedule.objects.all().filter(deadline__lt=date)
        for schedule in schedules:
            schedule.delete()
    except:
        pass


class Command(BaseCommand):
    help = "runs the discord bot"

    def handle(self, *args, **options):
        print("Importing modules dynamically")
        modules = glob.glob(join(dirname(__file__), "bot", "mods", "*.py"))

        for f in modules:
            if isfile(f) and not f.endswith("__init__.py"):
                print("    %s ..." % basename(f)[:-3], end="")
                modules = import_module(
                    ".bot.mods." + basename(f)[:-3], "accounts.management.commands"
                )
                print("[OK]")
            print("")

        print("Commands Loaded")
        print_commands()
        print("")
        print("Runtime!")

        client.run(settings.DISCORD_BOT_TOKEN)