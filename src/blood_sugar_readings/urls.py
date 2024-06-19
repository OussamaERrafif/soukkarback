from flask import Blueprint
from . import controllers

readings_blueprint = Blueprint('readings', __name__)

# Routes for BloodSugarReading model
readings_blueprint.route('/', methods=['GET'])(controllers.get_readings)
readings_blueprint.route('/<reading_id>', methods=['GET'])(controllers.get_reading)
readings_blueprint.route('/', methods=['POST'])(controllers.create_reading)
readings_blueprint.route('/<reading_id>', methods=['PUT'])(controllers.update_reading)
readings_blueprint.route('/<reading_id>', methods=['DELETE'])(controllers.delete_reading)
