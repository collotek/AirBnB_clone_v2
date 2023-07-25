#!/usr/bin/python3
"""Starts flask app and routes two requests

    Returns:
        string: normal strings
    """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c(text=None):
    return "C " + text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run()
