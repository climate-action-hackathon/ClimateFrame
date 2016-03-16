import schedule
import time

def job():
    print("Running scheduled job...")

def start_scheduled_jobs():
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
