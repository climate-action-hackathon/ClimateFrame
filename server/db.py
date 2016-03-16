from pymongo import MongoClient
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

    def get_recipes(self):
        db = self.get_db()
        return db.recipes

    def add_recipe(self, recipe):
        recipes = self.get_recipes()
        recipe_id = recipes.insert_one(recipe).inserted_id
        return recipe_id

    def get_all_recipes(self):
        recipes = self.get_recipes()
        return recipes
