import schedule
import time

def job():
    print("I'm working...")

def start_scheduled_jobs():
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    job()
    print("scheduling...")
    start_scheduled_jobs()
