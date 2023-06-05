import os;
import pandas as pd;
baseDir = os.path.join(os.path.dirname(__file__))

print(baseDir)

# pd.read_csv('/files/Sales_invoices_list.csv')
df = pd.read_csv(r"./files/Sales_invoice_list.csv")
# print(df.head())
w = df.rowone
x = df.rowtwo
y = df.rowthree
z = df.rowfour

for row1,row2,row3,row4 in zip(w,x,y,z):
    print(row1,row2,row3,row4)