#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """prints Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
"""route for /hbnb set to false"""
def hbnb():
    """return only HBNB"""
    return 'HBNB'
@app.route('/c/<text>', strict_slashes=False)
"""app route for c text"""
def cisfun(text):
    """ display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )"""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
