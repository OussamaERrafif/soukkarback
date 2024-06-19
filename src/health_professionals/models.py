from bson import ObjectId

class HealthProfessional:
    def __init__(self, name, specialization, contact_info, availability, user_ratings=None, reviews=None):
        self._id = ObjectId()  # Unique identifier for each health professional
        self.name = name
        self.specialization = specialization
        self.contact_info = {
            'email': contact_info.get('email'),
            'number': contact_info.get('number'),
            'location': contact_info.get('location')
        }
        self.availability = availability
        self.user_ratings = user_ratings if user_ratings else []
        self.reviews = reviews if reviews else []
