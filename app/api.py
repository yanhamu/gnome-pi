from app import app
from flask import jsonify

from flask import Flask
from flask_restful import Resource, Api

@app.route('/api/index')
def myview():
    return jsonify([1, 2, 3])

class HelloWorld(Resource):
    def get(self):
        return {'hello':'world'}