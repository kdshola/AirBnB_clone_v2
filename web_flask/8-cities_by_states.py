#!/usr/bin/python3
""" Flask app module """

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close():
    """ closes current session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_states():
    """ Lists all states sorted by name and all its cities"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == 'main':
    app.run(host='0.0.0.0')
