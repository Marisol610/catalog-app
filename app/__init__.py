#!/products/bin/env python3
# #coding-*- utf -*-
"""THIS IS ASSIGNMENT 3 FOR FSDI-111""" 




from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config["SECRET_KEY"] = "MYSUPERSECRETSTRING"


from app import routes