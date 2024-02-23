from flask import jsonify, request, url_for, flash
from werkzeug.utils import secure_filename
import os
from app.src.dao.post_dao import get_posts, add_post
from app.src.entities.posts import Post

def get_or_add_posts(request):
    if request.method == 'GET':
        return get_posts()
    elif request.method == 'POST':
        new_post_data = request.get_json()

        if 'image' in request.files:
            image_file = request.files['image']
            print(f'Received image file: {image_file.filename}')
            
            image_filename = secure_filename(image_file.filename)
            image_path = os.path.join('app/static/uploads', image_filename)

            try:
                image_file.save(image_path)
                new_post_data['image'] = url_for('static', filename=f'uploads/{Date.now}')
                flash('Image uploaded successfully!', 'success')
            except Exception as e:
                flash(f'Error uploading image: {str(e)}', 'error')
                print(f'Error uploading image: {str(e)}')

        new_post = Post(**new_post_data)
        return add_post(new_post), 201
    else:
        return 'Method not allowed', 405
