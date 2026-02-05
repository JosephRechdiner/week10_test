from pymongo import MongoClient
import os
import json

MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")


class MongoManager:
    def __init__(self):
        try:
            self.client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}")
            print("Connection established successfully!")
        except Exception as e:
            raise Exception(f"Could not establish connection, Error: {str(e)}")
        
    def get_client(self):
        return self.client
    
    def seed_data(self, path, db):
        try:
            with open(path) as file:
                data = json.load(file)
                db["collection"].insert_many(data)
            print("Data seeded successfully!")
        except Exception as e:
            raise Exception(f"Could not seed data, Error: {str(e)}")