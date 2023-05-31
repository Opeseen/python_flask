from flask import Blueprint, render_template, request, flash, redirect, url_for, session,g;
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash;
from . import db;
from flask_login import login_user,login_required,logout_user,current_user;
import time;

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        Username = request.form.get('username').title().strip()
        Password = request.form.get('password')

        user = User.query.filter_by(username=Username).first()
        if user:
            if check_password_hash(user.password, Password):
                flash('Login Successfully..', category='success')
                login_user(user,remember=True)
                return render_template('dashboard.html')
            else:
                flash('Wrong password entered..', category='error')
        else:
            flash('Username does not exists',category='error')
    return render_template('login.html')
    

@auth.route('/logout')
def logout():
    logout_user()
    return render_template('logout.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        FirstName = request.form.get('firstname').title().strip()
        LastName = request.form.get('lastname').title().strip()
        Username = request.form.get('username').title().strip()
        Password = request.form.get('password')
        email = request.form.get('email').title().strip()
        tosAgreement = request.form.get('tosAgreement').title().strip()

        user = User.query.filter_by(username=Username).first()
        print(user)
        if user:
            flash('Username Alredy Exists...',category='error')
        elif len(FirstName) < 3:
            flash('Firstname must be greater than 2 characters',category='error')
        elif len(LastName) < 3:
            flash('Lastname must be greater than 2 characters',category='error')
        elif len(Username) < 4:
            flash('Username must be greater than 3 characters',category='error')
        elif len(Password) < 5:
            flash('Password must be greater than 4 characters',category='error')
        elif len(email) < 10:
            flash('Email must be greater than 9 characters',category='error')
        else:
            new_user = User(email=email,first_name=FirstName,username=Username,last_name=LastName,tosAgreement=tosAgreement,password=generate_password_hash(Password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user,remember=True)
            flash('Account Ctreated Successfully!',category='success')
            return redirect(url_for('views.home'))
        
    return render_template('signup.html')