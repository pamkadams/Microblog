from flask import render_template, flash, redirect
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
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)
