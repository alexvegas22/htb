from flask import jsonify, request, Blueprint
from app.src.controllers.post_controller import get_or_add_posts

post_routes = Blueprint('post_routes', __name__)

@post_routes.route('/posts', methods=['GET', 'POST'])
def posts():
    return get_or_add_posts(request)
