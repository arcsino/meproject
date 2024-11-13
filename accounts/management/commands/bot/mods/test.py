from accounts.management.commands.bot.commands import resister_command
from asgiref.sync import sync_to_async
from accounts.models import CustomUser

@resister_command("[Hh]ow many")
async def sendCount(channel_name, message):
    current_known_people = await sync_to_async(_stats_count, thread_sensitive=True)()
    await message.channel.send("I know about %s people" % current_known_people)


def _stats_count():

    return CustomUser.objects.all().count()
