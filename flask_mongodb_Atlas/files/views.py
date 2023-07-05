from flask import Blueprint, render_template, flash, make_response, redirect, url_for, request;
import pandas as pd;
from . import note;
from bson.objectid import ObjectId

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


@views.route('/updateNotePage',methods=['GET'])
def updateNotePage():
    queryID = request.args.get('id')
    if queryID:
        result = note.find({"_id":ObjectId(queryID)})
        for x in result:
            status = x['status']
            id = x['_id']
            notes = x['note']
    return render_template('note_page.html', status=status,id=id,notes=notes)