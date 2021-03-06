from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(Form):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
