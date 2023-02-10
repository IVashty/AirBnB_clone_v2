#!/usr/bin/python3
"""
display more text but an integer this time
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Hello Wprld from flask"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """lets add HBNB to the url as path"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Simple variable"""
    text = text.replace("_", " ")
    return "C " + text


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python(text="is cool"):
    """default value"""
    text = text.replace("_", " ")
    return "Python " + text


@app.route("/number/<int:n>", strict_slashes=False)
def number(number):
    """Displays 'number is a integer' only if number  is an integer."""
    return "{} is a number".format(number)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(number):
    """
    display a html page with number if the variable number is an integer
    """
    return render_template("5-number.html", number=number)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
