from pymongo import MongoClient

client = MongoClient(host='localhost', port=27019)
db = client.test
collection = db.account

data = []

for s in collection.find():
    print(s)    



