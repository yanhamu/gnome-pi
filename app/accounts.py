from flask import g

def get_accounts():
    return g.user.get('accounts',[])
    
def create_new():
    accounts = g.user.get('accounts',[])
    index = _get_index(accounts)
    new_account = {'id':index, 'name':'new account', 'type':'fio'}
    accounts.append(new_account)
    
    g.db.users.update_one(
        { '_id':g.user['_id'] },
        { '$set': { 'accounts':accounts }}
    )
    
    return new_account
    
def _get_index(accounts):
    if len(accounts) == 0:
        return 1
    return max(accounts, key= lambda x:x['id'])['id']
