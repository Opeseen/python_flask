from flask import Blueprint, render_template, request, flash, redirect, url_for;
from datetime import datetime;
from . import note;
from pymongo import errors;

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


