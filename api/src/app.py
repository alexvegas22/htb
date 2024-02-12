from flask import Flask, request

app = Flask(__name__)

from markupsafe import escape
    
@app.route("/")
def hello_world():
    return "<h1>HTB</h1>"

@app.route("/chatroom")
def chatroom_join():
    return "<h1>HTB</h1>"


@app.route("/chatroom/<room>")
def chatroom():
    return "<h1>HTB</h1>"
