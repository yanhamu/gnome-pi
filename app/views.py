from flask import render_template
from app import app, auth

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Tom'}   
    posts = [
            {
                'author':{'nickname':'John'},
                'body': 'Beautiful day'
            },
            {
                'author': {'nickname':'Susan'},
                'body':'Avengers'
            }
            ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/signin', methods=['GET','POST'])
def signin():
    form = auth.signin()
    print(form.email)
    return render_template('signin.html', title='Sign in', form = form)
    
@app.route('/signup', methods=['GET','POST'])
def signup():
    return render_template('signup.html', title='Sign up')
   
@app.route('/account/<id>')
def account(id):
    return render_template('account.html', title='Account',id=id)
