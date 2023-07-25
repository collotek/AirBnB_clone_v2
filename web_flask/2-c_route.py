#!/usr/bin/python3
"""Starts flask app and routes two requests

    Returns:
        string: normal strings
    """
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c(text=None):
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    app.run()
