#!/usr/bin/python3
""" Script that starts a web application. """
from flask import Flask
from flask import render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Display 'n is a number' if n is a number. """
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Display web template if n is a number. """
    if not isinstance(n, int):
        return app.abort(404)
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run()
