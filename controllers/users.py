from flask_restful import Resource
from flask import request
from services import user

class User(Resource):
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']
        return user.create_user(email, password)
