from flask import Blueprint
from . import controllers

recipes_blueprint = Blueprint('recipes', __name__)

# Routes for Recipe model
recipes_blueprint.route('/', methods=['GET'])(controllers.get_recipes)
recipes_blueprint.route('/<recipe_id>', methods=['GET'])(controllers.get_recipe)
recipes_blueprint.route('/', methods=['POST'])(controllers.create_recipe)
recipes_blueprint.route('/<recipe_id>', methods=['PUT'])(controllers.update_recipe)
recipes_blueprint.route('/<recipe_id>', methods=['DELETE'])(controllers.delete_recipe)
