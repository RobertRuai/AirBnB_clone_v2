#!/usr/bin/python3
"""hello_route module"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """deallocates storage if exists"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_states():
    """lists all objects from states"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    """executes object code"""
    app.run(host='0.0.0.0', port=5000)
