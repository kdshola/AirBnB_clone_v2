#!/usr/bin/python3
""" Flask app module """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays “Hello HBNB!” """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays "HBNB” """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """ displays C followed by text
    Args:
        text (sgr): text to print
    """
    return f'C {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
