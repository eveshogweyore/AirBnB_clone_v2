#!/usr/bin/python3
""" Script that starts a web application. """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """home route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def home_hbnb():
    """hbnb return route"""
    return "HBNB"

@app.route("/c/", strict_slashes=False)
@app.route("/c/<text>", strict_slashes=False)
def cdisplay(text):
    """ Display text with C. """
    return "C {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run()
