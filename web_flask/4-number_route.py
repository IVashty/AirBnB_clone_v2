#!/usr/bin/python3
"""
display more text but an integer this time
"""
from flask import Flask, abort

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/")
@app.route("/python/<text>")
def python(text="is cool"):
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>")
def number(n):
    return f"{n} is a number"


@app.route("/number/<non_int:n>")
def not_a_number(n):
    abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
