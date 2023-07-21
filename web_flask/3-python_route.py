#!/usr/bin/python3
"""hello_route module"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """entry function"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """displays C followed by input text"""
    return "C " + text.replace('_', ' ')

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pycool(text="is cool"):
    """display “Python ”, followed by text"""
    return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    """executes object code"""
    app.run(host='0.0.0.0', port=5000)
