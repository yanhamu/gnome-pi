'''
dashboard main services
'''
import pymongo
from bson.objectid import ObjectId


def get_top(db, user_id):
    '''
    retrieves top 10 transactions
    '''
    account_id = get_account_id(db, user_id)
    return list(db.transactions
                .find({'_account_id': account_id})
                .sort('date', pymongo.DESCENDING)
                .limit(10))


def get_account_id(db, user_id):
    '''
    returns  first users account id
    '''
    account = list(db.accounts.find({'_user_id': user_id}).limit(1))[0]
    return account['_id']
