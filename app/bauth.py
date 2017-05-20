from functools import wraps
from flask import abort, request
import base64

''' Very simple basic authentication. Checks if there are credentials cookie and passes / returns 401 
'''
def bauth(fn):
    @wraps(fn)
    def decorator(*args, **kwargs):
        username, password = _getCookie(request)
        if username == None:
            abort(401)
            return None
        return fn(*args, **kwargs)
    return decorator

def _getCookie(request):
    try:
        cookie = request.cookies.get('bauth')
        return decode(cookie)
    except:
        return None, None
    
def _decode(s):
    s = base64.b64decode(s).decode().split(':')
    return s[0],s[1]
    
def _encode(email, password):
    s = '{0}:{1}'.format(email, password)
    return base64.b64encode(s.encode())
