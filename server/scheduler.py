from apis.trigger import control_all_recipes
import threading
import time
from db import Database

database = Database()

def start_scheduled_jobs():
    print
    print(time.ctime())
    recipes = database.get_all_recipes()
    control_all_recipes(recipes)
    threading.Timer(60, start_scheduled_jobs).start()
