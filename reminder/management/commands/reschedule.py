from django.core.management.base import BaseCommand
from ...models import Deadline
import datetime


class Command(BaseCommand):
    help = "今日のスケジュールを削除、新しい日付の追加"

    def handle(self, *args, **options):
        today = datetime.datetime.today()
        week_names = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
        week = week_names[today.weekday()]
        # 今日のスケジュールを削除
        try:
            endline = Deadline.objects.get(date=today)
            endline.delete()
        except:
            pass
        # 新しい日付を追加
        try:
            newday = Deadline(date=(today + datetime.timedelta(days=30)), week=week)
            newday.save()
        except:
            pass