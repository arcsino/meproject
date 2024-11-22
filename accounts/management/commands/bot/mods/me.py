from accounts.management.commands.bot.commands import resister_command
from asgiref.sync import sync_to_async
from reminder.models import Schedule, Category

import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@resister_command("!cntskd")
async def sendSchedule(channel_name, message):
    count = await sync_to_async(_num_of_schedules, thread_sensitive=True)()
    if count != None:
        await message.channel.send(f"現在スケジュールは{count}個あります。")
    else:
        await message.channel.send("エラーが発生しました。")

def _num_of_schedules():
    try:
        count = Schedule.objects.all().count()
        return count
    except:
        return None


@resister_command("!cntskd bycat")
async def sendSchedule(channel_name, message):
    context = await sync_to_async(_get_schedules_context, thread_sensitive=True)()
    if context != None:
        await message.channel.send(context)
    else:
        await message.channel.send("エラーが発生しました。")

def _get_schedules_context():
    try:
        categories = Category.objects.all()
        schedules = Schedule.objects.all()
        context = ""
        for c in categories:
            context += f"`{c.name}`：{schedules.filter(category=c).count()}個\n"
        return context
    except:
        return None