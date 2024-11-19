from flask import jsonify, request, Blueprint
from app.src.controllers.post_controller import *

post_routes = Blueprint('post_routes', __name__)

@post_routes.route('/<board>/posts', methods=['GET', 'POST'])
def board_posts(board):
    return get_or_add_posts(request,board)
