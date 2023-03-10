from flask import Flask
import os
import models.models as models

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


