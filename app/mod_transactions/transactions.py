'''
Handles all transaction manipulation
'''

import pymongo
from bson.objectid import ObjectId
from flask import g


def get_last_transactions(page):
    account_id = __get_account_id(g.db, g.user['_id'])
    return list(g.db
                .transactions
                .find({'_account_id': account_id})
                .skip(page * 10)
                .sort('date', pymongo.DESCENDING)
                .limit(10))


def get_transaction(transaction_id):
    return g.db.transactions.find_one({'_id': ObjectId(transaction_id)})


def __get_account_id(db, user_id):
    '''
    returns  first users account id
    '''
    account = db.accounts.find_one({'_user_id': user_id})
    return account['_id']
