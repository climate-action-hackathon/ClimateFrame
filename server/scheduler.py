import schedule
import time
from db import Database

database = Database()

def job():
    print("Running scheduled job...")
    recipes = database.get_all_recipes()
    for recipe in recipes:
        print recipe

def start_scheduled_jobs():
    job()
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
