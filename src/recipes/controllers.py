from flask import request, jsonify
from bson.objectid import ObjectId
from src import db
from .models import Recipe

def get_recipes():
    recipes = list(db.recipes.find())
    for recipe in recipes:
        recipe['_id'] = str(recipe['_id'])
    return jsonify(recipes)

def get_recipe(recipe_id):
    recipe = db.recipes.find_one({'_id': ObjectId(recipe_id)})
    if recipe:
        recipe['_id'] = str(recipe['_id'])
        return jsonify(recipe)
    else:
        return jsonify({'error': 'Recipe not found'}), 404

def create_recipe():
    data = request.get_json()
    new_recipe = Recipe(
        name=data['name'],
        description=data['description'],
        ingredients=data['ingredients'],
        instructions=data['instructions'],
        nutritional_info=data['nutritional_info'],
        category=data['category']
    )
    db.recipes.insert_one(new_recipe.__dict__)
    return jsonify({'message': 'Recipe created successfully'}), 201

def update_recipe(recipe_id):
    data = request.get_json()
    db.recipes.update_one({'_id': ObjectId(recipe_id)}, {'$set': data})
    return jsonify({'message': 'Recipe updated successfully'})

def delete_recipe(recipe_id):
    db.recipes.delete_one({'_id': ObjectId(recipe_id)})
    return jsonify({'message': 'Recipe deleted successfully'})
