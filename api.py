from flask import Flask
from flask_restful import Api

from controllers import users, todos, authentication

app = Flask(__name__)
api = Api(app)

##
## Actually setup the Api resource routing here
##
api.add_resource(todos.TodoList, '/todos')
api.add_resource(todos.Todo, '/todos/<todo_id>')
api.add_resource(users.User, '/users')
api.add_resource(authentication.Authentication, '/gettoken')


if __name__ == '__main__':
    app.run(debug=True)