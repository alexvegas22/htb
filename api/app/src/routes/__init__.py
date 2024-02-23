#/src/routes
from flask import Blueprint

post_routes = Blueprint('post_routes', __name__)

image_routes = Blueprint('images_routes', __name__)

from app.src.routes.post_routes import *
from app.src.routes.images_routes import *
