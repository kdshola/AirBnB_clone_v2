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


@app.route('/states', strict_slashes=False)
def list_states():
    """ Lists all states sorted by name and all its cities"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('states/<id>', strict_slashes=False)
def list_states_by_id(id):
    """ displays a state if id matches given id """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state)


if __name__ == 'main':
    app.run(host='0.0.0.0')
