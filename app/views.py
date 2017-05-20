from flask import render_template, redirect, flash, request, g
from app import app, auth, bauth
from pymongo import MongoClient

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET','POST'])
def login():
    form = auth.LogInForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if bauth.checkuser(email, password):
            response = redirect('/dashboard')
            response.set_cookie('bauth', bauth.encode(email, password))
            return response
        flash('invalid credentials')
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
    db = MongoClient().client.gnomeDb
    g.db = db

