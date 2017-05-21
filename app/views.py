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
        email, password = form.email.data, form.password.data
        if bauth.check_user(email, password):
            resp = redirect('/dashboard')
            resp.set_cookie('bauth', bauth.encode(email, password))
            return resp
        flash('invalid credentials')
    return render_template('login.html', title='Log in', form=form)
    
@app.route('/logout', methods=['GET'])
@bauth.bauth
def logout():
    resp = redirect('/index')
    resp.set_cookie('bauth', '', expires=0)
    return resp

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = auth.LogInForm()
    if form.validate_on_submit():
        email, password = form.email.data, form.password.data
        if not bauth.isfree(email):
            flash('email is already registered')
            return render_template('signup.html', title='Sign up', form=form)
        bauth.create_new(email, password)
        resp = redirect('/dashboard')
        resp.set_cookie('bauth', bauth.encode(email, password))
        return resp
    return render_template('signup.html', title='Sign up', form=form)
   
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
    g.user = bauth.try_to_get_user()

