from accounts.management.commands.bot.commands import resister_command
from asgiref.sync import sync_to_async
from accounts.models import CustomUser
from reminder.models import Schedule

import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@resister_command("!send schedule")
async def sendSchedule(channel_name, message):
    id = await sync_to_async(_get_schedule_id, thread_sensitive=True)(message.author.id)
    url = await sync_to_async(_get_schedule_url, thread_sensitive=True)()
    content = await sync_to_async(_get_schedule_content, thread_sensitive=True)(message.author.id)

    embed = discord.Embed(
        title=("スケジュール #%s" % id),
        color=0x349961,
        description=content,
        url=url,
    )
    embed.set_thumbnail(url=message.guild.icon.url)
    embed.set_footer(
        text=("Send by %s" % message.author.display_name),
        icon_url=message.author.avatar.url,
    )
    await message.channel.send(embed=embed)


def _get_schedule_id(discord_id):
    try:
        user = CustomUser.objects.all().get(discord_id=discord_id)
        return user.schedule_id
    except:
        return "None"

def _get_schedule_url():
    return "https://example-dlksjflsjdfls.com"

def _get_schedule_content(discord_id):
    try:
        user = CustomUser.objects.all().get(discord_id=discord_id)
        schedule = Schedule.objects.all().get(pk=user.schedule_id)
        content = f"`カテゴリー`：{schedule.category.name}\n`教科`：{schedule.subject.name}\n`タイトル`：{schedule.title}\n`詳細`：{schedule.detail}\n`締め切り日`：{schedule.deadline}"
        return content
    except:
        return "None"