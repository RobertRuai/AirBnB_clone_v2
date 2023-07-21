#!/usr/bin/python3
"""hello_route module"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """entry function"""
    return "Hello HBNB!"

if __name__ == "__main__":
    """executes object code"""
    app.run(host='0.0.0.0', port=5000)
