#!/usr/bin/python3
""" Script that starts a Flask web application. """
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello HBNB!"

@app.route("/hbnb")
def home_hbnb():
    return "HBNB"

@app.route("/c/<text>")
def c_display(text):
    return f"C {text.replace("_", " ")}"


if __name__ == "__main__":
    app.run()
