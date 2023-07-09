from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify;
from datetime import datetime;
from . import noteCollection;
from pymongo import errors;
from . import models

auth = Blueprint('auth',__name__)

# Route function to create a note
@auth.route('/create_note',methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        defaultNoteStatus = 'UNCOMPLETED'
        NOTE = request.form.get('note').upper().strip()
        if len(NOTE) > 150:
            flash("Length of Note can't be greater than 150 Characters",category='error')
        else:
            try:
                now = datetime.now()
                date = now.strftime("%B %d, %Y %H:%M:%S")
                noteCollection.insert_one({'note':NOTE, 'status':defaultNoteStatus , 'date':date})
                flash(' Note Successfully Added.',category='success')
                return redirect(url_for('auth.create_note'))
            except Exception as e:
                flash('Error Encountered while adding your note... Contact Admin Support',category='error')
    
    return render_template('create_note.html')

# Route function to delete note
@auth.route('/deleteNote',methods=['POST'])
def deleteNote():
    if request.method == 'POST':
        payload = request.json['ids']
        if payload:
            payload = payload.split(',')
            try:
                for id in payload:
                    models.deleteNote(id)
                response = jsonify('<span class=\'flash green\'>Note has been successfully deleted</span>')
                response.status_code = 200
                return response
            except Exception as e:
                response = jsonify('<span class=\'flash red\'>OOPS, an internal error occur during deletion</span>')
                response.status_code = 500
                return response
            
        else:
            response = jsonify('<span class=\'flash red\'>OOPS, something went wrong</span>')
            response.status_code = 400
            return response


# Route function to update note
@auth.route('/updateNote',methods=['POST'])
def updateNote():
    if request.method == 'POST':
        payload = request.json['data']
        if payload:
            id = payload['note_id']
            notes = payload['note'].upper()
            status = payload['status']
            updateNote = models.updateNote(id,notes,status)
            if updateNote:
                response = jsonify('<span class=\'flash green\'>Note has been successfully updated.</span>')
                response.status_code = 200
                return response
            else:
                response = jsonify('<span class=\'flash green\'>An internal error occur while updating your note</span>')
                response.status_code = 500
                return response
        else:
            response = jsonify('<span class=\'flash red\'>OOPS, something went wrong</span>')
            response.status_code = 400
            return response