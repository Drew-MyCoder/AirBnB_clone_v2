#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
"""name of flask app hasn't been set"""

@app.route('/', strict_slashes=False)
def index():
"""message that is printed""""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hello_world():
"""message that is printed""""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
