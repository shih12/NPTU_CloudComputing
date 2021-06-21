from pymongo import MongoClient

def list_account():
    client = MongoClient(host='rs1', port=27041)

    db = client.test

    collection = db.account
    
    data = []
    for post in collection.find():
        data.append(data)

    return data
    
    