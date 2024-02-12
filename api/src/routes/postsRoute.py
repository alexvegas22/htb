from flask import Flask, request
from models import posts
app = Flask(__name__)

@app.get('/posts')
def login_get():
    return getPosts()

@app.post('/posts')
def login_post():
    return createPost()
