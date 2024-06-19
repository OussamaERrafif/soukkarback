from flask import Flask
from pymongo import MongoClient
from src.config import Config
from flask_cors import CORS

# Initialize Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Connect to MongoDB using MongoClient
client = MongoClient(app.config['MONGO_URI'])
db = client[app.config['DATABASE_NAME']]

# Enable CORS
CORS(app)

# Import and register blueprints for different modules
from  src.users.urls import users_blueprint
from  src.blood_sugar_readings.urls import readings_blueprint
from  src.recipes.urls import recipes_blueprint
from  src.health_professionals.urls import professionals_blueprint

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(readings_blueprint, url_prefix='/readings')
app.register_blueprint(recipes_blueprint, url_prefix='/recipes')
app.register_blueprint(professionals_blueprint, url_prefix='/professionals')
