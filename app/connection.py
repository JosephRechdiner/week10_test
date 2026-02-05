from pymongo import MongoClient
import os
import json

MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")

class MongoManager:
    client = None
    def __init__(self):
        try:
            if MongoManager.client is None:
                MongoManager.client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}")
                print("Connection established successfully!")
        except Exception as e:
            raise Exception(f"Could not establish connection, Error: {str(e)}")
        self.client = MongoManager.client

    def get_client(self):
        return self.client
    
    def seed_data(self, path, database):
        try:
            with open(path) as file:
                data = json.load(file)
                database["collection"].insert_many(data)
            print("Data seeded successfully!")
        except Exception as e:
            raise Exception(f"Could not seed data, Error: {str(e)}")