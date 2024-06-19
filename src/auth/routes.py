import bcrypt
from flask import Blueprint, request, jsonify, current_app
from src import db
from src.users.models import User
from src.auth.utils import generate_token, verify_token

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate email
    if not User.validate_email(data['email']):
        return jsonify({'error': 'Invalid email format'}), 400
    
    # Check for existing user
    existing_user = db.users.find_one({'email': data['email']})
    if existing_user:
        return jsonify({'error': 'Email already registered'}), 400

    # Ensure all required fields are present
    required_fields = ['name', 'email', 'password', 'age', 'gender', 'height', 'weight', 'medical_conditions', 'preferences', 'goals']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400
    
    new_user = User(
        name=data['name'],
        email=data['email'],
        password=data['password'],
        age=data['age'],
        gender=data['gender'],
        height=data['height'],
        weight=data['weight'],
        medical_conditions=data['medical_conditions'],
        preferences=data['preferences'],
        goals=data['goals']
    )
    db.users.insert_one(new_user.__dict__)
    return jsonify({'message': 'User registered successfully'}), 201

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = db.users.find_one({'email': data['email']})

    if user:
        user_obj = User(
            _id=user['_id'],
            name=user['name'],
            email=user['email'],
            age=user['age'],
            gender=user['gender'],
            height=user['height'],
            weight=user['weight'],
            medical_conditions=user['medical_conditions'],
            preferences=user['preferences'],
            goals=user['goals']
        )

        input_password = data['password']
        stored_password_hash = user['password']

        print(f"Input Password: {input_password}")
        print(f"Stored Password Hash: {stored_password_hash}")

        if bcrypt.checkpw(input_password.encode('utf-8'), stored_password_hash.encode('utf-8')):
            token = generate_token(data['email'])
            return jsonify({'token': token}), 200
        else:
            print("Password validation failed")

    
    return jsonify({'error': 'Invalid credentials'}), 401

@auth_blueprint.route('/logout', methods=['POST'])
def logout():
    # Placeholder for logout logic
    return jsonify({'message': 'Logged out successfully'}), 200
