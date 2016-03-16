from pymongo import MongoClient
import json

class Database():

    def __init__(self):
        self.client = None

    def connect(self):
        self.client = MongoClient()
        self.client = MongoClient("mongodb://127.0.0.1:27017/")

        return self.client

    def query(self):

        current_client = self.connect()
        db = current_client.cf
        cursor = db.content.find()
        results = {}

        for document in cursor:
            results[document['_id']] = document

        return results