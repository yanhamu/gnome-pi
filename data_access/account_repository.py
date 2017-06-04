"""account repository"""


class AccountRepository:
    """Account repository"""

    def __init__(self, database, user_id):
        self.database = database
        self.user_id = user_id

    def create_account(self, account):
        """creates new account"""
        
