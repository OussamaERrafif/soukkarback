from datetime import timedelta


class Config:
    
    # MongoDB configuration
    MONGO_URI = 'mongodb+srv://oussamaerra:oussamaerra@soukkar.oxhp94u.mongodb.net/?retryWrites=true&w=majority&appName=soukkar'
    DATABASE_NAME = 'soukkar'

    # JWT configuration
    JWT_SECRET_KEY = 'skar'  # Change this to a secure random key for production
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)  # Example: Token expires in 1 day
