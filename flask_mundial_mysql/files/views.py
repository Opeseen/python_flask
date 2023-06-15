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
    # for rows in record:
    #     id = rows.id
    #     po_number = rows.po_number
    #     invoice_number = rows.invoice_number
    #     invoice_date = rows.invoice_date
    #     due_date = rows.due_date

    # df = pd.DataFrame(id,columns=['id'])
    return render_template('dashboard.html', data=record)


# def getInvoices():
#     record = Record.query.all()
#     return record

# @views.route('/download')
# def download():
#     df = pd.DataFrame(list(getInvoices()))
#     print(df)
#     response = make_response(df.to_csv(index=False))
#     response.headers["Content-Disposition"] = "attachment; filename=data.csv"
#     response.headers["Content-Type"] = "text/csv"
#     return response

# @views.context_processor
# def context_processor():
#     return dict(getAll = getInvoices)











# @views.route('/')
# def home():
#     return render_template('home.html')


# @views.route('/dashboard')
# def dashboard():
#     record = Record.query.all()
#     df = pd.read_csv(r"./files/Sales_invoice_list.csv")
#     w = df.rowone
#     x = df.rowtwo
#     y = df.rowthree
#     z = df.rowfour
#     return render_template('dashboard.html', data1=w, data2=x, data3=y, data4=z, zip=zip)
