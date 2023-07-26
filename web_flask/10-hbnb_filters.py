#!/usr/bin/python3
"""hello_route module"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """deallocates storage if exists"""
    storage.close()


@app.route("/hbnb_ilters", strict_slashes=False)
def list_states():
    """displays hbnb html page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")

    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


if __name__ == "__main__":
    """executes object code"""
    app.run(host='0.0.0.0', port=5000)
