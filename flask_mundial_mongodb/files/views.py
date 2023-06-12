from flask import Blueprint, render_template, flash,redirect, url_for;
import pandas as pd;
from . import invoice;

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html')


@views.route('/dashboard')
def dashboard():
    try:
        all_invoice = invoice.find()
        return render_template('dashboard.html',all_invoice=all_invoice)
    except:
        flash('Could not fetch PO details...',category='error')

    return render_template('dashboard.html')

    


