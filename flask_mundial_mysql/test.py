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