from flask import jsonify
from redis import Redis
import json

redis = Redis(host='localhost', port=6379)

def get_new_board_index(board):
    return redis.llen(board)

from app.src.entities.posts import Post



def get_board_posts(board):
    posts_from_redis = redis.lrange(board, 0, -1)
    posts_list = [json.loads(post.decode()) for post in posts_from_redis]
    return jsonify(posts_list[::-1])

def add_post(new_post,board):
    post_dict = new_post.to_dict()
    json_data = json.dumps(post_dict)
    redis.rpush(board, json_data)
    return jsonify(post_dict)


    
