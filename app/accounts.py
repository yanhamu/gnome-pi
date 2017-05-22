from flask import g
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from bson.objectid import ObjectId

class AccountForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])

def get_accounts():
    id = g.user['_id']
    userId = id if isinstance(id, ObjectId) else ObjectId(id)
    return g.db.accounts.find({"_user_id":userId})
    
def create_new():
    user_id = g.user['_id']
    new_account = {'_user_id':user_id, 'name':'new account', 'type':'fio'}    
    inserted = g.db.accounts.insert_one(new_account)
    return inserted.inserted_id

def get_account(id):
    accountId = id if isinstance(id, ObjectId) else ObjectId(id)
    
    return g.db.accounts.find_one({"_id":accountId})

def remove_account(id):
    accountId = id if isinstance(id, ObjectId) else ObjectId(id)

    result = g.db.accounts.delete_one({'_id':accountId})    
    return
    
def update(id, account):
    toUpdate = get_account(id)
    toUpdate['name'] = account['name']
    g.db.accounts.update_one(
        {'_id':toUpdate['_id']},
        {'$set':{
            'name':toUpdate['name']
        }}
    )
