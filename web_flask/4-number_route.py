#!/usr/bin/python3
"""
display more text but an integer this time
"""
from flask import Flask, abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    text = text.replace("_", " ")
    return "C " + text


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python(text="is cool"):
    text = text.replace("_", " ")
    return "Python " + text


@app.route("/number/<int:number>", strict_slashes=False)
def number(number):
    """Displays 'number is a number' only if nunber is an integer."""
    return "{} is a number".format(number)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
