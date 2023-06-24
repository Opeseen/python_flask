import os;
import pandas as pd;
from datetime import date;
import numpy as np;
baseDir = os.path.join(os.path.dirname(__file__))

print(baseDir)

# pd.read_csv('/files/Sales_invoices_list.csv')
df = pd.read_csv(r"./files/Sales_invoice_list2.csv")
# print(df.head())
# df.info()
df.date = pd.to_datetime(df.date)
# df.info()

today_date = date.today()
print(today_date)
print(df.head())
today_date = pd.to_datetime(today_date)
df['new'] = (today_date - df.date) / np.timedelta64(1, 'D')
print(df.head())
print(df.info())

for x in df.new:
    if x > 300:
        print(True)
    else:
        print(False)

# print(df)
# w = df.rowone
# x = df.rowtwo
# y = df.rowthree
# z = df.rowfour

# for row1,row2,row3,row4 in zip(w,x,y,z):
#     print(row1,row2,row3,row4)



# @views.route('/dashboard')
# def dashboard():
#     record = Record.query.all()
#     df = pd.read_csv(r"./files/Sales_invoice_list.csv")
#     w = df.rowone
#     x = df.rowtwo
#     y = df.rowthree
#     z = df.rowfour
#     return render_template('dashboard.html', data1=w, data2=x, data3=y, data4=z, zip=zip)




# MYSQL Connection Section

# @views.route('/')
# def home():
#     return render_template('home.html')

# @views.route('/dashboard')
# def dashboard():
#     cursor.execute("SELECT po_number,invoice_number,invoice_date,due_date FROM student.record;")
#     result = cursor.fetchall()
#     print(result)
#     # for row in result:
    #     print(row[1])
    #     print(row)

    # return render_template('dashboard.html')



# <!-- 
# {% for row1,row2,row3,row4 in zip(data1,data2,data3,data4) %}
#   <tr>
#     <td>{{row1}}</td>
#     <td>{{row2}}</td>
#     <td>{{row3}}</td>
#     <td>{{row4}}</td>
#   </tr>
# {% endfor %} -->