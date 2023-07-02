from flask import Flask
from pymongo import MongoClient, errors;

uri = "mongodb+srv://admin:admin1234@atlascluster.bzgngel.mongodb.net/?retryWrites=true&w=majority"

try:
    client = MongoClient(uri)
    db = client.NotesDB
    note = db.record
    client.server_info()

    def create_app():
        app = Flask(__name__)
        app.config['SECRET_KEY'] = 'admin'
        
        from .views import views
        from .auth import auth

        app.register_blueprint(views,url_prefix='/')
        app.register_blueprint(auth,url_prefix='/')

        return app

except errors.ServerSelectionTimeoutError as err:
    print('Connection Error')
    print(err)