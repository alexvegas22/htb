from flask import jsonify
from redis import Redis

redis = Redis(host='localhost', port=6379)

def get_posts():
    posts_from_redis = redis.lrange('posts', 0, -1)
    posts_list = [json.loads(post.decode()) for post in posts_from_redis]
    return jsonify(posts_list)

def add_post(new_post):
    redis.rpush('posts', jsonify(new_post))
    return jsonify(new_post)
