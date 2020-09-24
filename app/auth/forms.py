from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField, TextAreaField 
from wtforms.validators import Required, Email, EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    username = StringField('Enter your username', validators=[Required()])
    password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Sign Up')
    

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired("Please enter your email address.")])
    password = PasswordField("Password", validators=[DataRequired("Please enter a password.")])
    submit = SubmitField("Sign In")