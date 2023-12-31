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
        text (str): text to print
    """
    return f'C {text}'


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def display_text_with_space(text):
    """ displays Python followed by text
    Args:
        text (str): text to print
    """
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def print_number(n):
    """ displays an integer n
    Args:
        n (int): number to display
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def print_number_h1(n):
    """ displays an integer n
    Args:
        n (int): number to display
    """
    return f'''\
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    </BODY>
        <h1>Number: {n}</h1>
    <BODY>
</HTML>'''


if __name__ == '__main__':
    app.run(host='0.0.0.0')
