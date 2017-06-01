"""Module takes care of all authentication stuff"""

import base64


class Authentication:
    """Takes care of authentication stuff"""

    def get_token(self, username, password):
        """retrieved token for correct password
        otherwise returns null
        """
        return self.__encode(username, password)

    def validate_token(self, token):
        """validates token, True if ok, False otherwise"""
        try:
            username, password = self.__decode(token)
            # call db and check that shit
        except:
            return False

    def __encode(self, email, password):
        """Returns encoded email and password"""
        formatted = '{0}:{1}'.format(email, password)
        return base64.b64encode(formatted.encode())

    def __decode(self, token):
        """Returns (email, password) tuple"""
        decoded = base64.b64decode(token).decode().split(':')
        return decoded[0], decoded[1]
