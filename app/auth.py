from flask_wtf import Form
from wtforms import PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

def signin():
    form = SignInForm()
    return form
    

class SignInForm(Form):
    email = EmailField('Email address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
