from flask import jsonify
from app.dao.post_dao import get_posts, add_post
from app.entities.post import Post

def get_or_add_posts(request):
    if request.method == 'GET':
        return get_posts()
    elif request.method == 'POST':
        new_post_data = request.get_json()
        new_post = Post(**new_post_data)
        return add_post(new_post), 201
    else:
        return 'Method not allowed', 405
