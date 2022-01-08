from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import requests, json

class RegistrationForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    mname = StringField('Middle Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),
                                                                    EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = requests.get(f'http://127.0.0.1:5000/existing_username/{username.data}')
        data =  user.json()
        if data != {}:
            existing = data['username']
        else:
            existing = False
        if existing:
            raise ValidationError("That username has already taken! Please choose a different one.")

    def validate_email(self, email):
        user = requests.get(f'http://127.0.0.1:5000/existing_email/{email.data}')
        data =  user.json()
        if data != {}:
            existing = data['email']
        else:
            existing = False
        if existing:
            raise ValidationError("That email has already taken! Please choose a different one.")
    
class LoginForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    mname = StringField('Middle Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    image = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = requests.get(f'http://127.0.0.1:5000/existing_username/{username.data}')
            data =  user.json()
            if data != {}:
                existing = data['username']
            else:
                existing = False
            if existing:
                raise ValidationError("That username has already taken! Please choose a different one.")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = requests.get(f'http://127.0.0.1:5000/existing_email/{email.data}')
            data =  user.json()
            if data != {}:
                existing = data['email']
            else:
                existing = False
            if existing:
                raise ValidationError("That email has already taken! Please choose a different one.")

