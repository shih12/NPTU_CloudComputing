from typing import Collection
from pymongo import MongoClient


def sql(name,password):
    client = MongoClient(host='localhost', port=27018)
    db = client.test
    collection = db.account
    
    username = str(name)
    passwd = str(password)

    test = collection.find({"name": username,"password": passwd}).count()

    print(test)