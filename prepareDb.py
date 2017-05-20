from pymongo import MongoClient

client = MongoClient()
db = client.gnomeDb
users = db.users
users.create_index([('email', pymongo.ASCENDING)],unique=True)
