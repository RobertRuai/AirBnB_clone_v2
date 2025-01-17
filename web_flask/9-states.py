#!/usr/bin/python3
"""hello_route module"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """deallocates storage if exists"""
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states<id>", strict_slashes=False)
def states(state_id=None):
    """lists all states objects"""
    states = storage.all("State")

    if state_id is not None:
       state_id = "State." + state_id
    return render_template("9-states.html", states=states, state_id=state_id)


if __name__ == "__main__":
    """executes object code"""
    app.run(host='0.0.0.0', port=5000)
