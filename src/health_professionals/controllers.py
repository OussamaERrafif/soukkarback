from flask import request, jsonify
from bson.objectid import ObjectId
from src import db
from .models import HealthProfessional

def get_professionals():
    professionals = list(db.professionals.find())
    for professional in professionals:
        professional['_id'] = str(professional['_id'])
    return jsonify(professionals)

def get_professional(professional_id):
    professional = db.professionals.find_one({'_id': ObjectId(professional_id)})
    if professional:
        professional['_id'] = str(professional['_id'])
        return jsonify(professional)
    else:
        return jsonify({'error': 'Health professional not found'}), 404

def create_professional():
    data = request.get_json()
    new_professional = HealthProfessional(
        name=data['name'],
        specialization=data['specialization'],
        contact_info=data['contact_info'],
        availability=data['availability']
    )
    db.professionals.insert_one(new_professional.__dict__)
    return jsonify({'message': 'Health professional created successfully'}), 201

def update_professional(professional_id):
    data = request.get_json()
    db.professionals.update_one({'_id': ObjectId(professional_id)}, {'$set': data})
    return jsonify({'message': 'Health professional updated successfully'})

def delete_professional(professional_id):
    db.professionals.delete_one({'_id': ObjectId(professional_id)})
    return jsonify({'message': 'Health professional deleted successfully'})
