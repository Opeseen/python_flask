from flask import Flask
from flask_sqlalchemy import SQLAlchemy;
import os;

baseDir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

DB_NAME = "database.db3"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'admin'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(baseDir, 'database.db3')
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://Horpeyemi:yomex5055@localhost/student'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User,Record

    create_database(app)

    return app

def create_database(app):
    with app.app_context():
        db.create_all()
        print('Database Created') 


