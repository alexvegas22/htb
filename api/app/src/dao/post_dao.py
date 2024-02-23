from flask import jsonify
from redis import Redis
import json
from app.src.entities.posts import Post


redis = Redis(host='localhost', port=6379)

def get_posts():
    posts_from_redis = redis.lrange('posts', 0, -1)
    posts_list = [json.loads(post.decode()) for post in posts_from_redis]
    return jsonify(posts_list)

def add_post(new_post):
    post_dict = new_post.to_dict()
    json_data = json.dumps(post_dict)  # Serialize the dictionary to a JSON string
    redis.rpush('posts', json_data)
    return jsonify(post_dict)

