from flask import jsonify, request
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from app.src.dao.post_dao import *
from app.src.entities.posts import Post

def get_or_add_posts(request, board):
    if request.method == 'GET':
        return get_board_posts(board)
    elif request.method == 'POST':
        new_post_data = request.form.to_dict()
        new_post_data['board'] = board

        if 'image' in request.files:
            image_file = request.files['image']
            print(f'Received image file: {image_file.filename}')

            _, file_extension = os.path.splitext(image_file.filename)

            # Generate a unique filename based on the current timestamp and file extension
            image_filename = f'{datetime.now().timestamp()}{file_extension}'
            image_path = os.path.join('app/static/uploads', board, image_filename)
            
            new_post_data['image'] = str(image_filename)

            try:
                os.makedirs(os.path.dirname(image_path), exist_ok=True)
                image_file.save(image_path)
                new_post = Post(**new_post_data)
                return add_post(new_post, board), 201
            except Exception as e:
                print(f'Error uploading image: {str(e)}')

        else :
            return jsonify({"error": "Missing image file"}), 400
                
    else:
        return jsonify({"error": "Method not allowed"}), 405 
 
