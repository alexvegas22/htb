#/src/routes
from flask import Blueprint

# Create a blueprint for post-related routes
post_routes = Blueprint('post_routes', __name__)

# Import the routes from post_routes.py
from app.routes.post_routes import *
