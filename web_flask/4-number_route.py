#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)
"""name of flask not set"""


@app.route('/', strict_slashes=False)
def index():
    """message to be printed"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """messsage to be printed"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
"""value of c text""""
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
"""python value"""
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
