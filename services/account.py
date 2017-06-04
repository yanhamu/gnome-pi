"""Future implementation of Account Service"""

from data_access.account_repository import AccountRepository


class AccountService:
    def __init__(self, database, user_id):
        self.database = database
        self.user_id = user_id
        self.account_repository = AccountRepository(database, user_id)

    def create_account(self, account):
        return 123
