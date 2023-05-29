from flask import Flask
from flask_sqlalchemy import SQLAlchemy;
import os;

baseDir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'admin'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(baseDir, 'database.db')
    db.init_app(app)

    from .views import views
    from .auth import auth

    from .models import User,Note

    create_database(app)

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    return app

def create_database(app):
    if not os.path.exists('files/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Database Created')