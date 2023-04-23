#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)
"""this flask hasn't been given a name. """

@app.route('/', strict_slashes=False)
"""strict_slashes has been set to false in the route"""
def hello_hbnb():
	"""message to be printed"""
	return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
