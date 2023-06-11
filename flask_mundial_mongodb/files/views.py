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
    df = pd.read_csv(r"./files/Sales_invoice_list.csv")
    w = df.rowone
    x = df.rowtwo
    y = df.rowthree
    z = df.rowfour
    return render_template('dashboard.html', data1=w, data2=x, data3=y, data4=z, zip=zip)




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

