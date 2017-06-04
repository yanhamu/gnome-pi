"""Handles /gettoken requests"""
from flask_restful import Resource
from flask import request, g
import base64
import services.authentication


def try_to_get_user():
    token = request.headers.get('BAUTH', default=None)
    if token == None:
        return None
    email, password = __decode(token)
    if email is None or password is None:
        return None
    return g.db.users.find_one({'email': email})


def __decode(token):
    try:
        email, password = base64.b64decode(token).decode().split(':')
        return email, password
    except:
        return None, None


def __encode(email, password):
    return base64.b64encode('{0}:{1}'.format(email, password))


class Authentication(Resource):
    """Authentication resource"""

    def post(self):
        """generates token if possible"""
        json = request.get_json()
        username = json['email']
        password = json['password']

        auth = services.authentication.Authentication()
        token = auth.get_token(username, password)

        if token is None:
            return '', 401
        else:
            return str(token)
