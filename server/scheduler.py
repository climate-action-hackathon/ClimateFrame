import schedule
import time
from db import Database

database = Database()

def is_triggering(trigger):
    return True

def job():
    recipes = database.get_all_recipes()
    for recipe in recipes:
        print('Controlling recipe id ' + recipe['_id'])
        trigger = recipe['triggers'][0]
        action = recipe['actions'][0]
        if is_triggering(trigger):
            print('Going to do the following action:')
            print(action)
            

def start_scheduled_jobs():
    job()
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
