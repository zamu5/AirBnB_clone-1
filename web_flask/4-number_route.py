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


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
     method that returns a message when look for localhost:5000/hbnb
    """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def variable(text):
    """
    This method handle a variable text
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_message(text="is cool"):
    """
    python is cool
    """
    return "Python {}".format(text.replace('_', ' ') if text is not "is cool"
                              else text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    handle if number is an int
    """
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run()
