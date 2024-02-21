from flask import Flask
from app.routes.postRoutes import post_routes

app = Flask(__name__)
CORS(app,resources={"/*":{"origins":"*"}})
app.register_blueprint(post_routes)

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
    {'id' : 3,
       'title' :'Funny monkey',
       'img' :"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhc_l6f9V0b-0pU_CjVpplngWFbB0JFP0Uhw&usqp=CAU",
       'user':'veal',
       'content' :'Teehee this monkey is so silly!!! "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."'},
  ]



def getPosts():
    return posts

def createPost(post):
     return posts.append(post)
