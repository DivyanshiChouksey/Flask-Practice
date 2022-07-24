# https://flask.palletsprojects.com/en/2.1.x/quickstart/

from flask import Flask

app = Flask(__name__)


@app.route("/")  # add /-index page starting page
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/<name>")
def test(name):
    return f"Hello, {name}!"
