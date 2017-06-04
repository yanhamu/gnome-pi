from functools import wraps
import controllers.authentication
from flask import g
import flask


def auth(fn):
    @wraps(fn)
    def decorator(*args, **kwargs):
        print("#")
        print(g.user)
        if g.user is None:
            return flask.make_response("", 401)
        return fn(*args, **kwargs)
    return decorator
