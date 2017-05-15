from flask import render_template
from app import app

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
