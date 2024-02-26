from flask import jsonify, request, url_for
from werkzeug.utils import secure_filename
import os
from app.src.dao.post_dao import *
from app.src.entities.posts import Post

def get_or_add_posts(request,board):
    if request.method == 'GET':
        return get_board_posts(board)
    elif request.method == 'POST':
        new_post_data = request.get_json()
        new_post_data['board'] = board

        if 'image' in request.files:
            image_file = request.files['image']
            print(f'Received image file: {image_file.filename}')
            
            image_filename = secure_filename(image_file.filename)
            image_path = os.path.join('app/static/uploads', board, image_filename)

            try:
                image_file.save(image_path)
                new_post_data['image'] = url_for(filename=f'{board}/{datetime.now().timestamp()}')
            except Exception as e:
                print(f'Error uploading image: {str(e)}')

        new_post = Post(**new_post_data)
        return add_post(new_post,board), 201
    else:
        return 'Method not allowed', 405
