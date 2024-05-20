#!/usr/bin/python3
""" Script that starts a web application. """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def home_hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cdisplay(text):
    """ Display text with C. """
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_display(text="is_cool"):
    """ Display text with python. """
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run()
