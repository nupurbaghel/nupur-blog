import os

__author__ = "Nupur Baghel"

import pymongo



class Database(object):
    #URI= "mongodb://127.0.0.1:27017"
    URI= os.environ.get("MONGODB_URI")
    DATABASE=None

    @staticmethod
    def initialise():
        client=pymongo.MongoClient(Database.URI)
        #Database.DATABASE=client['Python']
        Database.DATABASE=client.get_default_database()

    @staticmethod
    def insert(collection,data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
