from flask import jsonify
from redis import Redis
import os
import json

redis_host = os.getenv("REDIS_HOST","http://htb-redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis = Redis(host=redis_host, port=redis_port)

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


    
