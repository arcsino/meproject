from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

def reschedule():
   """
   This function is called by start() below
   """
   print('Update!')

# new=>
def start():
   """
   Scheduling data update
   Run update function once every 12 seconds
   """
   scheduler = BackgroundScheduler()
   
   scheduler.add_job(reschedule, 'cron',  hour=23, minute=59) # schedule
   scheduler.start()