'''
Handles all transaction manipulation
'''

from bson.objectid import ObjectId
from flask import g


def get_transaction(transaction_id):
    return g.db.transactions.find_one({'_id': ObjectId(transaction_id)})
