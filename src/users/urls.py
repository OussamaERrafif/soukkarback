from flask import Blueprint
from . import controllers

users_blueprint = Blueprint('users', __name__)

# Routes for User model
# users_blueprint.route('/', methods=['GET'])(controllers.get_users)
# users_blueprint.route('/<user_id>', methods=['GET'])(controllers.get_user)
users_blueprint.route('/', methods=['POST'])(controllers.create_user)
users_blueprint.route('/<user_id>', methods=['PUT'])(controllers.update_user)
users_blueprint.route('/<user_id>', methods=['DELETE'])(controllers.delete_user)
