from flask import g
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class AccountForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])

def get_accounts():
    return g.user.get('accounts',[])
    
def create_new():
    accounts = _get_accounts()
    index = _get_index(accounts)
    new_account = {'id':index, 'name':'new account', 'type':'fio'}
    accounts.append(new_account)
    
    g.db.users.update_one(
        { '_id':g.user['_id'] },
        { '$set': { 'accounts':accounts }}
    )
    
    return new_account

def get_account(id):
    accounts = _get_accounts()
    account = list(filter(lambda x: x['id']==id, accounts))
    return account[0]

def remove_account(id):
    accounts = _get_accounts()
    removed = list(filter(lambda x: x['id']==id, accounts))
    g.db.users.update_one(
        {'_id': g.user['id'] },
        {'$set':{ 'accounts':removed }}
    )
    return
    
def _get_index(accounts):
    if len(accounts) == 0:
        return 1
    return max(accounts, key= lambda x:x['id'])['id']
    
def _get_accounts():
    return g.user.get('accounts',[])
