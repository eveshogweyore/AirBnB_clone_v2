#!/usr/bin/python3
""" Script that starts a Flask web application. """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ The home page. """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def home_hbnb():
    """ The HBNB page. """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_display(text):
    """
    The C display page.

    Parameter
    ---------
        text: the last string of the url
    """
    return f"C {text.replace("_", " ")}"


if __name__ == "__main__":
    app.run()
