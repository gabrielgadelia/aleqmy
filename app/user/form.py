from flask_wtf import *
from wtforms import *
from wtforms.fields import *
from wtforms.validators import *


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[email(), data_required()],
                       render_kw={'class': 'form-control', 'placeholder': 'Enter Email'})
    password = PasswordField('Password', validators=[data_required()],
                             render_kw={'class': 'form-control', 'placeholder': 'Enter Password'})
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = EmailField('Email', validators=[email(), data_required()],
                       render_kw={'class': 'form-control', 'placeholder': 'Enter Email'})
    password = PasswordField('Password', validators=[data_required()],
                             render_kw={'class': 'form-control', 'placeholder': 'Enter Password'})
    first_name = StringField('First Name', validators=[data_required()],
                             render_kw={'class': 'form-control', 'placeholder': 'Enter First Name'})
    last_name = StringField('Last Name', validators=[data_required()],
                            render_kw={'class': 'form-control', 'placeholder': 'Enter Last Name'})
    age = IntegerField('Age', validators=[data_required()],
                       render_kw={'class': 'form-control', 'placeholder': 'Enter Age'})
    address = StringField('Address',
                          render_kw={'class': 'form-control', 'placeholder': 'Enter Address'})
    submit = SubmitField('Sign In', render_kw={'class': 'btn btn-primary'})

