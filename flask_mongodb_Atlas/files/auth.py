from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify;
from datetime import datetime;
from . import note;
from pymongo import errors;
from . import models

auth = Blueprint('auth',__name__)


@auth.route('/create_note',methods=['GET', 'POST'])
def create_po():
    if request.method == 'POST':
        defaultNoteStatus = 'UNCOMPLETED'
        NOTE = request.form.get('note').upper().strip()
        if len(NOTE) > 300:
            flash("Length of Note can't be greater than 300 Characters",category='error')
        else:
            try:
                now = datetime.now()
                date = now.strftime("%B %d, %Y %H:%M:%S")
                note.insert_one({'note':NOTE, 'status':defaultNoteStatus , 'date':date})
                flash(' Note Successfully Added...',category='success')
                return redirect(url_for('auth.create_po'))
            except Exception as e:
                flash('Error Encountered while adding your note... Contact Admin Support',category='error')
    
    return render_template('create_note.html')


@auth.route('/deleteSelected',methods=['POST'])
def delete():
    if request.method == 'POST':
        payload = request.json['ids']
        if payload:
            payload = payload.split(',')
            print(payload)
            try:
                for id in payload:
                    models.deleteNote(id)
                response = jsonify('<span class=\'flash green\'>Your note has been successfully deleted</span>')
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









    # if request.method == 'POST':
    #     payload = request.json['ids']
    #     if payload:
    #         print(payload)
    #         response = jsonify('<span class=\'flash green\'>Response successfully returned</span>')
    #         response.status_code = 200
	# 		return response
    #     else:
    #         response = jsonify('<span class=\'flash red\'>OOPS, something went wrong</span>')
    #         response.status_code = 400
	# 		return response