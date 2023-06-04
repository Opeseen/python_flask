from flask import Blueprint, render_template;
from mysql.connector import Error;
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




# MYSQL Connection Section

# @views.route('/')
# def home():
#     return render_template('home.html')

# @views.route('/dashboard')
# def dashboard():
#     cursor.execute("SELECT po_number,invoice_number,invoice_date,due_date FROM student.record;")
#     result = cursor.fetchall()
#     print(result)
#     # for row in result:
    #     print(row[1])
    #     print(row)

    # return render_template('dashboard.html')

