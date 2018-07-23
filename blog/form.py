from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, TextAreaField
from wtforms.fields.html5 import EmailField
from flask_blog.blog.models import Category
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class SetupForm(FlaskForm):
    name = StringField('Blog name', validators=[validators.DataRequired(),
                                                validators.Length(max=80)])
    fullname = StringField('Full name', [validators.Required()])
    email = EmailField('Email', [validators.Required()])
    username = StringField('Username', [
        validators.DataRequired(),
        validators.Length(min=4, max=25)
    ])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=4, max=80)
    ])
    confirm = PasswordField('Repeat password')


def categories():
    return Category.query


class PostForm(FlaskForm):
    title = StringField('Title', [
        validators.DataRequired(),
        validators.Length(max=80)
    ])
    body = TextAreaField('Content', [
        validators.DataRequired()
    ])
    category = QuerySelectField('Category', query_factory=categories, allow_blank=True)
    new_category = StringField('New Category')

