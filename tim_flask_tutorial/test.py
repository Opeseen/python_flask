from flask import Flask
from flask_sqlalchemy import SQLAlchemy;
from sqlalchemy_utils import database_exists
import pymysql;

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:password@flask-db.cgsgjuurrxyy.us-east-1.rds.amazonaws.com/users"
db.init_app(app)


class Data(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(15))
    last_name = db.Column(db.String(15))
    email = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(20))    
    # notes = db.relationship('Note')


with app.app_context():
  new_user = Data(email='Opeyemi5055@yahoo.com',first_name='Opeyemi',last_name='Alabi',password='jembe')
  db.session.add(new_user)
  db.session.commit()

  db.create_all()
  print('Database Created')


