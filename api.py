from flask import Flask, g
from flask_restful import Api
from pymongo import MongoClient

from controllers import users, todos, authentication, accounts

app = Flask(__name__)
api = Api(app)

##
## Actually setup the Api resource routing here
##
api.add_resource(todos.TodoList, '/todos')
api.add_resource(todos.Todo, '/todos/<todo_id>')
api.add_resource(users.User, '/users')
api.add_resource(accounts.AccountController, '/accounts')
api.add_resource(authentication.Authentication, '/gettoken')

@app.before_request
def before_request():
    g.db = MongoClient().gnomeDb
    g.user = authentication.try_to_get_user()

if __name__ == '__main__':
    app.run(debug=True)