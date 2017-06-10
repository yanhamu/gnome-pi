from flask import Flask, g, render_template, redirect, flash, request
from flask_restful import Api
from pymongo import MongoClient

from controllers import users, todos, authentication, accounts

flask_app = Flask(
    __name__,
    template_folder='app',
    static_path='/app',
    static_url_path='app',
    static_folder='app')
api = Api(flask_app)


@flask_app.route('/')
@flask_app.route('/index')
def index():
    return flask_app.send_static_file('index.html')


##
# Actually setup the Api resource routing here
##
api.add_resource(todos.TodoList, '/todos')
api.add_resource(todos.Todo, '/todos/<todo_id>')
api.add_resource(users.User, '/users')
api.add_resource(accounts.AccountController, '/accounts')
api.add_resource(authentication.Authentication, '/gettoken')


@flask_app.before_request
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
    flask_app.run(debug=True)
