import pymongo
from bson.objectid import ObjectId

def get_top(db, accountId):
    return list(db.transactions.find().limit(10))
