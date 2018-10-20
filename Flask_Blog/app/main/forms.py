from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField , PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email
from .. import db
from ..models.users import User

EqualTo('confirm', message='Passwords must match')

class SignUp(FlaskForm):

    username = StringField('Enter Your Name: ' , validators= [Length(3,50), DataRequired()])
    email = StringField('Enter Yor Email: ', validators= [Email()])
    password = PasswordField('Enter Your Password: ' ,validators= [Length(3,50), DataRequired()])
    confirm_password = PasswordField('Enter Your Password Again: ' ,validators= [Length(3,50), DataRequired(), EqualTo('password', message='Passwords must match')])
    remember = BooleanField('Remember Me')
    Submit = SubmitField('Sign Up !')
'''
    def validate_user(self, Username):

        user = User.query.filter_by(username = Username.data).first()
        if user:
            raise ValidationError('Username Already Taken')
    def validate_email(self, email):

        email = User.query.filter_by(email = email.data).first()
        if email:
            raise ValidationError('Email Already in Use')
'''
class Login(FlaskForm):

    username = StringField('Enter Your Name: ' , validators= [Length(3,50), DataRequired()])
    email = StringField('Enter Yor Email: ', validators= [Email()])
    password = PasswordField('Enter Your Password: ' ,validators= [Length(3,50), DataRequired()])
    Submit = SubmitField('Login')

    
    
    
