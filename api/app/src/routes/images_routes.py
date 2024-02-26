from flask import render_template, request, redirect, flash, Blueprint, send_from_directory, jsonify
import os
from werkzeug.utils import secure_filename
from app.app import app

# Use the app.root_path to get the root directory of the Flask app
upload_folder = os.path.join(app.root_path, 'static', 'uploads')

images_routes = Blueprint('images_routes', __name__)

@app.route('/<board>/<filename>')
def get_image(board,filename):
    file_path = board+'/'+filename
    return send_from_directory(upload_folder, file_path)

@images_routes.route('/images')
def list_images():
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder, exist_ok=True)

    image_files = [f for f in os.listdir(upload_folder) if os.path.isfile(os.path.join(upload_folder, f))]

    # Return the list of images as JSON
    return jsonify({'images': image_files})
