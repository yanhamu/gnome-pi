from flask import Flask, g
from flask_restful import Api
from pymongo import MongoClient

from controllers import users, todos, authentication, accounts

app = Flask(__name__)
api = Api(app)

##
# Actually setup the Api resource routing here
##
api.add_resource(todos.TodoList, '/todos')
api.add_resource(todos.Todo, '/todos/<todo_id>')
api.add_resource(users.User, '/users')
api.add_resource(accounts.AccountController, '/accounts')
api.add_resource(authentication.Authentication, '/gettoken')


@app.before_request
def init_request():
    """initializes database connection and user if possible"""
    g.db = get_db_connection()
    g.user = get_user_data()


def get_user_data():
    """retrieves user if possible"""
    return authentication.try_to_get_user()

def get_db_connection():
    """initializes database connection"""
    return MongoClient().gnomeDb


if __name__ == '__main__':
    app.run(debug=True)
