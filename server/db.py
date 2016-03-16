from pymongo import MongoClient
from bson.objectid import ObjectId
import json

class Database():

    def __init__(self):
        self.client = None

    def connect(self):
        self.client = MongoClient()
        self.client = MongoClient("mongodb://127.0.0.1:27017/")
        return self.client

    def get_db(self):
        current_client = self.connect()
        return current_client.recipes

    def get_cursor_data(self, cursor):
        data = []
        for item in cursor:
            data.add(item)
        return data

    def add_recipe(self, recipe):
        db = self.get_db()
        recipe_id = db.recipes.insert_one(recipe).inserted_id
        return recipe_id

    def get_all_recipes(self):
        db = self.get_db()
        cursor = db.recipes.find()
        recipes = self.get_cursor_data(cursor)
        return recipes

    def get_recipe(self, id):
        db = self.get_db()
        objectid = ObjectId(id)
        cursor = db.recipes.find({"__id":objectid})
        # recipes = self.get_cursor_data(cursor)
        return cursor

