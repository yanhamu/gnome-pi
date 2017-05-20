from flask import render_template, redirect, flash, request
from app import app, auth, bauth

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

@app.route('/login', methods=['GET','POST'])
def login():
    form = auth.LogInForm()
    if form.validate_on_submit():
        flash('maybe')
        response = redirect('/dashboard')
        response.set_cookie('bauth','xxx')
        return response
    return render_template('login.html', title='Log in', form=form)
    
@app.route('/signup', methods=['GET','POST'])
def signup():
    return render_template('signup.html', title='Sign up')
   
@app.route('/account/<id>')
@bauth.bauth
def account(id):
    return render_template('account.html', title='Account', id=id)
    
@app.route('/dashboard')
@bauth.bauth
def dashboard():
    return render_template('dashboard.html')
    
@app.before_request
def before_request():
    print('before request')
    

