from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from accounts.models import CustomUser, DiscordUser
from asgiref.sync import sync_to_async

import discord
from discord import app_commands

from os.path import dirname, basename, isfile, join
from importlib import import_module
import glob

from .bot.commands import print_commands, find_commands


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


@tree.command(name='active', description='Display active button.')
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("### アクティブボタンを表示しました！", ephemeral=True)
    await interaction.channel.send(view=ActiveButton())


class ActiveButton(discord.ui.View):
    def __init__(self):
        super().__init__()
    
    @discord.ui.button(label="Become Active!", style=discord.ButtonStyle.green, row=4)
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
        except:
            return "### サインアップはしましたか？"

    # ユーザーネームが変更されたユーザーならば変更
    try:
        dun = DiscordUser.objects.all().get(username=username)
    except:
        dun = DiscordUser.objects.all().get(discord_id=discord_id)
        dun.username = username
        dun.save()

    # アクティブ化済みユーザーにはエラーメッセージ
    if cu.is_active:
        return "### あなたのアカウントは無事アクティブ化されました。"


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