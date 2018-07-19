from flask_blog import app
from flask import render_template, redirect, url_for, request, session
from flask_blog.author.form import RegisterForm, LoginForm
from flask_blog.author.models import Author


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None

    if form.validate_on_submit():
        author = Author.query.filter_by(
            username=form.username.data,
            password=form.password.data
        ).limit(1)
        if author.count():
            session['username'] = form.username.data
            return redirect(url_for('login_success'))
    return render_template('author/login.html', form=form, error=error)


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        return redirect(url_for('success'))
    return render_template('author/register.html', form=form)


@app.route('/success')
def success():
    return 'Success'

@app.route('/login_success')
def login_success():
    return 'Author logged in'


