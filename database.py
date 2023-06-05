from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()

username = os.getenv('USER')
password = os.getenv('DATAPASSKEY')

class database():
    def __init__(self):
        self.uri = f"mongodb+srv://{username}:{password}@clipsurf.upczxaf.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        try:
            self.client.admin.command('ping')
        except Exception as e:
            return "Error"
        self.db = self.client["Email_data"]
        self.collection = self.db['Survey']

    def insert(self,val):
        try:
            self.collection.insert_one(val)
            return True
        except:
            return False

    def update(self,query,val):
        try:
            newval={"$set":val}
            self.collection.update_one(query,newval)
            return True
        except:
            return False
