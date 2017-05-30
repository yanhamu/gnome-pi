'''
    Contains basic routes and passes control to appropriate services
'''

from flask import render_template, redirect, flash, g
from app import app, auth, bauth, accounts, dashboard
from pymongo import MongoClient


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
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


@app.route('/signup', methods=['GET', 'POST'])
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


@app.route('/accounts', methods=['GET'])
@bauth.bauth
def accounts_index():
    model = accounts.get_accounts()
    return render_template('accounts.html', model=model)


@app.route('/accounts', methods=['POST'])
@bauth.bauth
def accounts_create():
    new_account = accounts.create_new()
    return redirect('accounts/{0}'.format(new_account))


@app.route('/accounts/<id>', methods=['GET', 'POST'])
@bauth.bauth
def account(id):
    account = accounts.get_account(id)
    form = accounts.AccountForm()
    if form.validate_on_submit():
        accounts.update(id, {
            'name': form.name.data,
            'token': form.token.data
        })
    else:
        if len(form.errors) > 0:
            flash(form.errors)
        form.name.data = account['name']
        form.token.data = account['token']

    return render_template('account.html', title='Account', form=form, id=id)


@app.route('/accounts/<id>/delete', methods=['POST'])
@bauth.bauth
def remove_account(id):
    accounts.remove_account(id)
    return redirect('/accounts')


@app.route('/accounts/<account_id>/transactions')
@bauth.bauth
def index_transactions(account_id):
    return render_template('transactions.html')


@app.route('/transactions/<transaction_id>')
@bauth.bauth
def transaction_detail(transaction_id):
    return render_template('transaction.html')


@app.route('/dashboard')
@bauth.bauth
def dashboard_index():
    data = dashboard.get_top(g.db, g.user['_id'])
    print(len(data))
    return render_template('dashboard.html', data=data)


@app.route('/reports')
@bauth.bauth
def reports_index():
    '''
    records management
    '''
    return render_template('reports.html')


@app.route('/draft-report')
@bauth.bauth
def draft_report():
    '''
    handles simple draft report
    proof of concept
    '''
    d = {
        'labels': ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
        'datasets': [
            {
                'label': 'revenue',
                'data': [10, 10, 12, 10, 12, 12, 14],
                'backgroundColor':"rgba(31, 236, 8, 0.4)"},
            {
                'label': 'expences',
                'data': [9, 11, 11, 10, 12, 11, 12],
                'backgroundColor': "rgba(241, 37, 18, 0.4)"},
            {
                'label': 'gain',
                'data': [1, -1, 1, 0, 0, 1, 2],
                'backgroundColor': "rgba(63, 127, 191, 0.4)"}]
    }

    return render_template('draft-report.html', data=d)


@app.before_request
def before_request():
    '''
    prepares global objects
    '''
    db = MongoClient().gnomeDb
    g.db = db
    g.user = bauth.try_to_get_user()
