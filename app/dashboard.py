'''
dashboard main services
'''
import pymongo


def get_account_id(db, user_id):
    '''
    returns  first users account id
    '''
    account = list(db.accounts.find({'_user_id': user_id}).limit(1))[0]
    return account['_id']
