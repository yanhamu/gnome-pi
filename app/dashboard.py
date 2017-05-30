'''
dashboard main services
'''
import pymongo


def get_top(db, user_id, page=0):
    '''
    retrieves top 10 transactions
    '''
    account_id = get_account_id(db, user_id)
    return list(db.transactions
                .find({'_account_id': account_id})
                .skip(page * 10)
                .sort('date', pymongo.DESCENDING)
                .limit(10))


def get_account_id(db, user_id):
    '''
    returns  first users account id
    '''
    account = list(db.accounts.find({'_user_id': user_id}).limit(1))[0]
    return account['_id']
