#!/usr/bin/python3
"""Starts up a flask application
Returns:
    str: Hello HBNB!
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
