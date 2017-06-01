from flask_restful import Resource
from flask import request


class User(Resource):
    def post(self):
        username = request.json['username']
        password = request.json['password']
        return {'u': username, 'p': password}
