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


if __name__ == "__main__":
    app.run()
