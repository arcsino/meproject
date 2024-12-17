from django.core.management.base import BaseCommand
from discord_webhook import DiscordWebhook, DiscordEmbed
from ...models import Schedule
import datetime


def webhook(url, color, description, id):
    webhook = DiscordWebhook(url=url)
    embed = DiscordEmbed(title=f"スケジュール #{id}", description=description, color=color, url=f"https://arcsino.pythonanywhere.com/reminder/schedules/detail/{id}/")
    embed.set_thumbnail(url="https://arcsino.pythonanywhere.com/static/images/photo1.png")
    webhook.add_embed(embed)
    response = webhook.execute()


class Command(BaseCommand):
    help = "今日のスケジュールを通知させる"

    def handle(self, *args, **options):
        today = datetime.datetime.today()
        try:
            schedules = Schedule.objects.filter(deadline__date=today).order_by("pk")
            for schedule in schedules:
                url = schedule.category.webhook_url
                color = schedule.category.embed_color
                fu = ""
                for fus in schedule.finished_user.all():
                    fu += f"{fus.nickname} "
                description = f"`カテゴリー`：{schedule.category.name}\n`教科`：{schedule.subject.name}\n`タイトル`：{schedule.title}\n`詳細`：{schedule.detail}\n`締め切り日`：{schedule.deadline.date}\n`完遂ユーザー`：{fu}\n"
                schedule_id = schedule.pk
                webhook(url=url, color=color, description=description, id=schedule_id)
        except:
            pass