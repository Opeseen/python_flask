from flask import Blueprint, render_template,request,flash,redirect,url_for;
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash;
from . import db;
from flask_login import login_user,login_required,logout_user,current_user;

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').title()
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully..', category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Wrong Password Entered..')
        else:
            flash('Email does not exists',category='error')
    return render_template('login.html',user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email').title()
        firstName = request.form.get('firstName').title()
        lastName = request.form.get('lastName').title()
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email alredy exists...',category='error')
        elif len(email) < 7:
            flash('Invalid Email Address',category='error')
        elif len(firstName) < 3:
            flash('Invalid Firstname',category='error')
        elif len(lastName) < 3:
            flash('Invalid Lastname',category='error')
        elif len(password1)  < 5:
            flash('Password character must be greater than 4',category='error')
        elif password1 != password2:
            flash('Password do not match',category='error')
        else:
            new_user = User(email=email,first_name=firstName,last_name=lastName,password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit() 
            flash('Signup Successfull',category='success')
            return redirect(url_for('views.home'))
    return render_template('signup.html',user=current_user)