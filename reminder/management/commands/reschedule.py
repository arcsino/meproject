from django.core.management.base import BaseCommand
from ...models import Deadline
import datetime


class Command(BaseCommand):
    help = "スケジュールの日程を一か月分作る"

    def handle(self, *args, **options):
        today = datetime.datetime.today()
        week_names = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
        for i in range(0, 30):
            date = today + datetime.timedelta(days=i)
            week = week_names[date.weekday()]
            try:
                newday = Deadline(date=date, week=week)
                newday.save()
            except:
                pass
        print("Rescheuled!!")