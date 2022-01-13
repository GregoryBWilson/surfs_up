# 9.4.3 Set Up Flask and Create a Route
# https://courses.bootcampspot.com/courses/1177/pages/9-dot-4-3-set-up-flask-and-create-a-route?module_item_id=356209
# Create a New Python (app.py) File and Import the Flask and other Dependencies
from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Set Up the Database
# We'll set up our database engine for the Flask application in much
# the same way we did for climate_analysis.ipynb, so most of this setup process will be familiar.
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

# Create Flask Routes
# First, we need to define the starting point, also known as the root. 
# Whenever you make a route in Flask, you put the code you want in that specific route below @app.route().
app = Flask(__name__)

# Greg is here
https://courses.bootcampspot.com/courses/1177/pages/9-dot-5-2-create-the-welcome-route?module_item_id=356225


