from flask import Blueprint, render_template, flash, make_response, redirect, url_for;
import pandas as pd;
from . import invoice;

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/dashboard')
def dashboard():  
    return render_template('dashboard.html')

def getInvoices():
    all_invoices = invoice.find()
    return all_invoices

@views.route('/download')
def download():
    df = pd.DataFrame(list(getInvoices()))
    response = make_response(df.to_csv(index=False))
    response.headers["Content-Disposition"] = "attachment; filename=data.csv"
    response.headers["Content-Type"] = "text/csv"
    return response

@views.context_processor
def context_processor():
    return dict(getAll = getInvoices)



    


