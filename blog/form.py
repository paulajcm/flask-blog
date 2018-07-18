from wtforms import StringField, validators
from flask_blog.author import RegisterForm


class SetupForm(RegisterForm):
    name = StringField('Blog name', validators=[validators.DataRequired(),
                                                validators.Length(max=80)])
    

