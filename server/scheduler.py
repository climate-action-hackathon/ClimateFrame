from apis.trigger import control_all_recipes
import schedule
import time
from db import Database

database = Database()

def job():
    recipes = database.get_all_recipes()
    control_all_recipes(recipes)

def start_scheduled_jobs():
    job()
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
