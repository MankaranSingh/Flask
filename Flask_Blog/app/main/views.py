from flask import render_template, session, redirect, url_for, flash, redirect
from . import main
from .forms import Login, SignUp
from .. import db
from ..models.users import User, Role
from werkzeug import check_password_hash, generate_password_hash
from flask_login import login_user
from werkzeug import generate_password_hash


@main.route('/Home')
def home():
    return render_template('HomePage.html')

@main.route('/Login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Logged In')
            redirect(url_for('home'))
        else:
            flash('Login Failed, Incorrect Username or Password Entered')
    return render_template('Login.html', form = form)

@main.route('/SignUp', methods=['GET', 'POST'])
def sign_up():
    form = SignUp()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username = form.username.data, email = form.email.data, password= hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your Acount has been successfuly registered')
        return redirect(url_for('login'))
    return render_template('Register.html', form = form)
                        
        
    
            
            
        
            
