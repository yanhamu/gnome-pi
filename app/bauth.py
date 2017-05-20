from functools import wraps
from flask import abort, request, g
import base64

''' Basic authentication decorator. Checks bauth cookie and passes / returns 401 
'''
def bauth(fn):
    @wraps(fn)
    def decorator(*args, **kwargs):
        email, password = _getCookie()
        if checkuser(email, password):
            g.user = g.db.users.find_one({'email':email})
            return fn(*args, **kwargs)
        else: 
            abort(401)
            return None
    return decorator

def checkuser(email, password):
    if email is None or password is None:
        return False
        
    users = g.db.users
    user = users.find_one({'email':email})
    if user:
        return _issame(user.password, password)
    else:
        return False
    
def encode(email, password):
    s = '{0}:{1}'.format(email, password)
    return base64.b64encode(s.encode())
    
def _issame(password, persistedPassword):
    return password == persistedPassword

def _getCookie():
    try:
        cookie = request.cookies.get('bauth')
        return decode(cookie)
    except:
        return None, None
    
def _decode(s):
    s = base64.b64decode(s).decode().split(':')
    return s[0],s[1]
