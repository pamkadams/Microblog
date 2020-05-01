from flask import render_template
from app import app
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)
