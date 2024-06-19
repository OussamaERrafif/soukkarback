from bson import ObjectId

class Recipe:
    def __init__(self, name, description, ingredients, instructions, nutritional_info, category, user_ratings=None, reviews=None):
        self._id = ObjectId()  # Unique identifier for each recipe
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions
        self.nutritional_info = nutritional_info
        self.category = category
        self.user_ratings = user_ratings if user_ratings else []
        self.reviews = reviews if reviews else []
