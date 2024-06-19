from flask import request, jsonify
from bson.objectid import ObjectId
from src import db
from .models import User
from src.auth.jwt import jwt_required



# def get_users():
#     users = list(db.users.find())
#     for user in users:
#         user['_id'] = str(user['_id'])
#     return jsonify(users)

# def get_user(user_id):
#     user = db.users.find_one({'_id': ObjectId(user_id)})
#     if user:
#         user['_id'] = str(user['_id'])
#         return jsonify(user)
#     else:
#         return jsonify({'error': 'User not found'}), 404


def create_user():
    data = request.get_json()
    new_user = User(
        clerkid=data['clerkid'],
        firstname=data['firstname'],
        lastname=data['lastname'],
        email=data['email'],
        age=data['age'],
        gender=data['gender'],
        height=data['height'],
        weight=data['weight'],
        medical_conditions=data['medical_conditions'],
        preferences=data['preferences'],
        goals=data['goals']
    )
    db.users.insert_one(new_user.__dict__)
    return jsonify({'message': 'User created successfully'}), 201

def update_user(user_id):
    data = request.get_json()
    db.users.update_one({'clerkid': user_id}, {'$set': data})
    return jsonify({'message': 'User updated successfully'})

def delete_user(user_id):
    db.users.delete_one({'clerkid': user_id})
    return jsonify({'message': 'User deleted successfully'})
