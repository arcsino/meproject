from django.core.management.base import BaseCommand
from django.conf import settings

from notice.models import EmbedMessage
from reminder.models import Schedule
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async

import discord
from discord import app_commands

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

    # スラッシュコマンドを同期
    await tree.sync()


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
    return f"https://arcsino.pythonanywhere.com/reminder/schedules/detail/{schedule_id}"


def _get_schedule_description(schedule_id):
    try:
        schedule = Schedule.objects.all().get(pk=schedule_id)
        description = f"`カテゴリー`：{schedule.category.name}\n`教科`：{schedule.subject.name}\n`タイトル`：{schedule.title}\n`詳細`：{schedule.detail}\n`締め切り日`：{schedule.deadline}"
        return description
    except:
        return None


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