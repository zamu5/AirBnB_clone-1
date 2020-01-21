#!/usr/bin/python3
"""
flask module
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def main():
    """
    method that returns a message when look for localhost:5000/
    """
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    """
     method that returns a message when look for localhost:5000/hbnb
    """
    return ("HBNB")


if __name__ == "__main__":
    app.run()
