from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Pam'}
    posts = [
        {
            'author': {'username': 'Laurie'},
            'body': 'Rainy day in Potomac!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'I am excited to use my outdoor TV!'
        },
        {
            'author': {'username': 'Denise'},
            'body': 'Fire Wok for dinner!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)

