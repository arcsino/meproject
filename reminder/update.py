from apscheduler.schedulers.background import BackgroundScheduler
from discord_webhook import DiscordWebhook, DiscordEmbed
from .models import Deadline, Schedule

import datetime

def reschedule():
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


def remind():
    today = datetime.datetime.today()
    try:
        schedules = Schedule.objects.filter(deadline__date=today).order_by("pk")
        for schedule in schedules:
            url = schedule.category.webhook_url
            color = schedule.category.embed_color
            description = f"`カテゴリー`：{schedule.category.name}\n`教科`：{schedule.subject.name}\n`タイトル`：{schedule.title}\n`詳細`：{schedule.detail}\n`締め切り日`：{schedule.deadline.date}\n"
            schedule_id = schedule.pk
            webhook(url=url, color=color, description=description, id=schedule_id)
    except:
        pass


def webhook(url, color, description, id):
    webhook = DiscordWebhook(url=url)
    embed = DiscordEmbed(title=f"スケジュール #{id}", description=description, color=color, url=f"https://arcsino.pythonanywhere.com/reminder/schedules/detail/{id}/")
    embed.set_thumbnail(url="https://arcsino.pythonanywhere.com/static/images/photo1.png")
    webhook.add_embed(embed)
    response = webhook.execute()


def start():
    scheduler = BackgroundScheduler()  
    scheduler.add_job(reschedule, 'cron',  hour=23, minute=59)
    scheduler.add_job(remind, 'cron',  hour=7, minute=0)
    scheduler.start()