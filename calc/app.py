from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def addition():
    """Add a and b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(add(a, b))

@app.route("/sub")
def subtraction():
    """Subtract b from a."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sub(a, b))

@app.route("/mult")
def multiplication():
    """Multiply a and b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(mult(a, b))

@app.route("/div")
def division():
    """Divide a by b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(div(a, b))




