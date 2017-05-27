import pymongo
from bson.objectid import ObjectId

def get_top(db, accountId):
    r = db.transactions.find().limit(10)
    print(list(r))
    print(accountId)
    return list(r)
