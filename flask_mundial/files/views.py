from flask import Blueprint, render_template;
# from mysql.connector import Error;
from .models import User, Record;
import pandas as pd;
views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html')


@views.route('/dashboard')
def dashboard():
    record = Record.query.all()
    return render_template('dashboard.html', data=record)


