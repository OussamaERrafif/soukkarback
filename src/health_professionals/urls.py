from flask import Blueprint
from . import controllers

professionals_blueprint = Blueprint('professionals', __name__)

# Routes for HealthProfessional model
professionals_blueprint.route('/', methods=['GET'])(controllers.get_professionals)
professionals_blueprint.route('/<professional_id>', methods=['GET'])(controllers.get_professional)
professionals_blueprint.route('/', methods=['POST'])(controllers.create_professional)
professionals_blueprint.route('/<professional_id>', methods=['PUT'])(controllers.update_professional)
professionals_blueprint.route('/<professional_id>', methods=['DELETE'])(controllers.delete_professional)
