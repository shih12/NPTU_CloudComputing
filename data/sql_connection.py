from pymongo import MongoClient

def connt(name,password):
    client = MongoClient(host='rs1', port=27041)

    db = client.test

    collection = db.account

    account={
        'name': name,
        'password': password
    }

    result = collection.insert_one(account)
    
    return result

