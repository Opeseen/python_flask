from flask import Blueprint, render_template, request, flash, redirect, url_for;
from datetime import datetime;
from . import invoice;

auth = Blueprint('auth',__name__)


@auth.route('/create_po',methods=['GET', 'POST'])
def create_po():
    if request.method == 'POST':
        PO_NUM = request.form.get('po_num').upper().strip()
        INV_NUM = request.form.get('inv_num').upper().strip()
        INV_DATE = request.form.get('inv_date')
        DUE_DATE = request.form.get('due_date')

        try:
            invoice.insert_one({'po_number':PO_NUM, 'invoice_number':INV_NUM, 'invoice_date':INV_DATE, 'due_date':DUE_DATE})
            flash(f'PO {PO_NUM} Successfully Added...',category='success')
            return redirect(url_for('auth.create_po'))
        except:
            flash(f'There was an error while adding the PO {PO_NUM}...',category='error')
    
    return render_template('create_po.html')


