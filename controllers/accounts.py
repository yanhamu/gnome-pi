from flask_restful import Resource
from flask import request
import services.account
from models.model import Account


class AccountController(Resource):
    '''Handles requests for account'''

    def post(self):
        '''creates new account'''

        data = request.get_json()
        name = data['name']
        token = data['token']
        account = Account(1, name, token)

        services.account.create_account(account)
        return '123'
