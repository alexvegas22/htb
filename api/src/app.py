from flask import Flask, request


app = Flask(__name__)

posts =  [
      {'id':1,
       'title' :'Dumbass cat',
       'img' :"https://external-preview.redd.it/_SAG0sDDTrhFv33-mJmfvBuA9sxKN4qq5X7Mbk-NztQ.jpg?auto=webp&s=bf2014f99fbda79ed9cd8fb4b9673e7ff09825f5",
       'user':'veal',
       'content' :'Look at this image of this cat. Why is he standing...'},
      {'id' : 2,
       'title' :'Strange dog',
       'img' :"https://i.redd.it/2adub8se2dlb1.jpg",
       'user':'veal',
       'content' :'Okay, this dog is kinda freaky'},
      
  ]

@app.route('/posts')
def getPosts():
    return posts
@app.post('/posts')
def login_post():
    return createPost()
