from . import db;
from flask_login import UserMixin;
from sqlalchemy.sql import func;

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(15),unique=True)
    first_name = db.Column(db.String(15))
    last_name = db.Column(db.String(15))
    password = db.Column(db.Text(150))
    date = db.Column(db.DateTime(timezone=True),default=func.now())

class Record(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    po_number = db.Column(db.String(15))
    invoice_date = db.Column(db.Date)
    due_date = db.Column(db.Date)
    invoice_number = db.Column(db.String(10),unique=True)
    date = db.Column(db.DateTime(timezone=True),default=func.now())



# MSQL Database Section

# import mysql.connector;
# from mysql.connector import Error;

# try:
#     connection = mysql.connector.connect(
#     host = "localhost",
#     user = "Horpeyemi",
#     password = "yomex5055",
#     database='student'
# )
#     print("MySQL Database connection successful")
# except Error as err:
#     print(f"Error: '{err}'")


# create_user_table = """
# CREATE TABLE IF NOT EXISTS User(
# Id INTEGER  AUTO_INCREMENT PRIMARY KEY,
# username VARCHAR(10),
# first_name VARCHAR(10),
# last_name VARCHAR(10),
# password TEXT(50)
# );
# """

# create_record_table = """
# CREATE TABLE IF NOT EXISTS Record(
# Id INTEGER AUTO_INCREMENT PRIMARY KEY,
# po_number VARCHAR(15),
# invoice_date DATE,
# due_date DATE,
# invoice_number VARCHAR(10)
# );
# """

# cursor = connection.cursor()

# cursor.execute(create_user_table)
# connection.commit()
# cursor.execute(create_record_table)
# connection.commit()