from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import discord

from os.path import dirname, basename, isfile, join
from importlib import import_module
import glob

from .bot.commands import print_commands, find_commands


intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


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

        client.run("")
        # client.run(settings.DISCORD['TOKEN'])
