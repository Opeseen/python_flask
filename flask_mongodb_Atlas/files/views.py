from flask import Blueprint, render_template, flash, make_response, redirect, url_for, request, flash;
import pandas as pd;
from . import noteCollection;
from bson.objectid import ObjectId
from . import models

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/dashboard')
def dashboard():
    getNotes = models.getNote()
    if getNotes:
        return render_template('dashboard.html', data=getNotes)
    else:
        error = "cound not load the note dashboard"
        return render_template('error.html',errorMessage = error)


@views.route('/download')
def download():
    getNotes = models.getNote()
    if getNotes:
        df = pd.DataFrame(list(getNotes))
        response = make_response(df.to_csv(index=False))
        response.headers["Content-Disposition"] = "attachment; filename=data.csv"
        response.headers["Content-Type"] = "text/csv"
        return response
    else:
        error = "cound not download the note"
        return render_template('error.html', errorMessage = error)


@views.route('/updateNotePage',methods=['GET'])
def updateNotePage():
    queryID = request.args.get('id')
    if queryID:
        result = noteCollection.find({"_id":ObjectId(queryID)})
        for x in result:
            status = x['status']
            id = x['_id']
            notes = x['note']
    return render_template('note_page.html', status=status,id=id,notes=notes)




# def getNote():
#     all_note = noteCollection.find()
#     return all_note

# @views.context_processor
# def context_processor():
#     return dict(data = getNote)