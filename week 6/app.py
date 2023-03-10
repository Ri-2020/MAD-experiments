from flask import Flask
from flask_restful import Api
import config as config
from database.configdb import db

app = None
api = None

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(config.LocalDatabaseConfig)
    api = Api(app)
    db.init_app(app)
    app.app_context().push()
    return app , api

app , api = create_app()

# from routes import *
from api import CourseAPI
api.add_resource(CourseAPI, "/api/course" , "/api/course/<string:course_id>")

if __name__ == "__main__":
    app.run()
