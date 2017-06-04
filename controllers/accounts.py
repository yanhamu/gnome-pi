from flask_restful import Resource
from flask import request, g
from services.account import AccountService
from models.model import Account
import basic_auth


class AccountController(Resource):
    '''Handles requests for account'''
    decorators = [basic_auth.auth]

    def post(self):
        '''creates new account'''

        data = request.get_json()
        name = data['name']
        token = data['token']
        account = Account(1, name, token)

        print(g.user)
        # mocking to be fixed

        service = AccountService(g.db, g.user['_id'])
        service.create_account(account)
        return '123'
