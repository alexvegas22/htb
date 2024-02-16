from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app,resources={"/*":{"origins":"*"}})


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
       'content' :'Teehee this monkey is so silly!!!'},
  ]

@app.route('/posts', methods=['GET','POST'])
def posts_route():
    # handle the POST request
    if request.method == 'POST':
        data = request.get_json()

        post = {
            'id': len(posts),
            'title': data['title'],
            'img': data['image'],
            'user': 'veal',
            'content': data['content']
        }
        print(post)
        createPost(post)
    # otherwise handle the GET request
    return getPosts()

def getPosts():
    return posts

def createPost(post):
     return posts.append(post)

if __name__ == "__main__":
    app.run(app, debug=True)
