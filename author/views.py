from flask_blog import app
from flask import render_template, redirect, url_for, request
from flask_blog.author.form import RegisterForm


@app.route('/login')
def login():
    return "welcome"


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        return redirect(url_for('success'))
    return render_template('author/register.html', form=form)


@app.route('/success')
def success():
    return 'Success'
