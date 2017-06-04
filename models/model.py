"""Contains default object definition"""


class Account:
    """Account model"""

    def __init__(self, user_id, name, token):
        """Default initializer"""
        self.user_id = user_id
        self.name = name
        self.token = token
