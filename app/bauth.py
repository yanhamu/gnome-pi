from functools import wraps
from flask import abort, request, g
import base64

''' Basic authentication decorator. Checks bauth cookie and passes / returns 401 
'''
def bauth(fn):
    @wraps(fn)
    def decorator(*args, **kwargs):
        if try_to_get_user():
            return fn(*args, **kwargs)
        else: 
            abort(401)
            return None
    return decorator

def try_to_get_user():
    email, password = _getCookie()
    if check_user(email, password):
        return g.db.users.find_one({'email':email})
    return None

def check_user(email, password):
    if email is None or password is None:
        return False
        
    user = g.db.users.find_one({'email':email})
    if user:
        return _issame(user['password'], password)
    else:
        return False

def isfree(email):
    if email is None:
        return False
    users = g.db.users
    user = users.find_one({'email':email})
    return user is None
    
def create_new(email, password):
    users = g.db.users.insert_one(
        {
            "email":email,
            "password":password
        })
    return
    
def encode(email, password):
    s = '{0}:{1}'.format(email, password)
    return base64.b64encode(s.encode())
    
def _issame(password, persistedPassword):
    return password == persistedPassword

def _getCookie():
    try:
        cookie = request.cookies.get('bauth')
        return _decode(cookie)
    except:
        return None, None
    
def _decode(s):
    s = base64.b64decode(s).decode().split(':')
    return s[0],s[1]
