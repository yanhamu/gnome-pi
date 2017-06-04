"""Handles /gettoken requests"""
from flask_restful import Resource
from flask import request
import services.authentication


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
