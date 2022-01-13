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

# Create a New Flask App Instance
app = Flask(__name__)

# Create Flask Routes
# First, we need to define the starting point, also known as the root.
# All of your routes should go after the app = Flask(__name__) line of code. Otherwise, your code may not run properly.
@app.route('/')

# Whenever you make a route in Flask, you put the code you want in that specific route below @app.route().

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
# The next route we'll build is for the precipitation analysis.
# This route will occur separately from the welcome route.

@app.route("/api/v1.0/precipitation")

# Create the precipitation() function.
# We'll use jsonify() to format our results into a JSON structured file.

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# Create the stations route
@app.route("/api/v1.0/stations")

# Create a function called Stations()
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Create the temperature observations route
@app.route("/api/v1.0/tobs")

# Create a function called temp_monthly()
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# To see the minimum, maximum, and average temperatures we'll create a route for our summary statistics report.
# This route is different from the previous ones in that we will have to provide both a starting and ending date.

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Next, create a function called stats() to put our code in.
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

