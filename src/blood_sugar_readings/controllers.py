from flask import request, jsonify
from bson.objectid import ObjectId
from src import db
from .models import BloodSugarReading

def get_readings():
    readings = list(db.readings.find())
    for reading in readings:
        reading['_id'] = str(reading['_id'])
    return jsonify(readings)

def get_reading(reading_id):
    reading = db.readings.find_one({'_id': ObjectId(reading_id)})
    if reading:
        reading['_id'] = str(reading['_id'])
        return jsonify(reading)
    else:
        return jsonify({'error': 'Reading not found'}), 404

def create_reading():
    data = request.get_json()
    new_reading = BloodSugarReading(
        user_id=data['user_id'],
        date=data['date'],
        time=data['time'],
        blood_sugar_level=data['blood_sugar_level'],
        notes=data['notes']
    )
    db.readings.insert_one(new_reading.__dict__)
    return jsonify({'message': 'Blood sugar reading created successfully'}), 201

def update_reading(reading_id):
    data = request.get_json()
    db.readings.update_one({'_id': ObjectId(reading_id)}, {'$set': data})
    return jsonify({'message': 'Blood sugar reading updated successfully'})

def delete_reading(reading_id):
    db.readings.delete_one({'_id': ObjectId(reading_id)})
    return jsonify({'message': 'Blood sugar reading deleted successfully'})
