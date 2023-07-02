from flask import Blueprint, render_template, flash, make_response, redirect, url_for;
import pandas as pd;
from . import note;

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/dashboard')
def dashboard():  
    return render_template('dashboard.html')

def getNote():
    all_note = note.find()
    return all_note

@views.route('/download')
def download():
    df = pd.DataFrame(list(getNote()))
    response = make_response(df.to_csv(index=False))
    response.headers["Content-Disposition"] = "attachment; filename=data.csv"
    response.headers["Content-Type"] = "text/csv"
    return response

@views.context_processor
def context_processor():
    return dict(data = getNote)



    


