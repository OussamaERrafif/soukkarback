from bson import ObjectId

class BloodSugarReading:
    def __init__(self, user_id, date, time, blood_sugar_level, notes):
        self._id = ObjectId()  # Unique identifier for each blood sugar reading
        self.user_id = ObjectId(user_id)  # ID of the user who logged the reading
        self.date = date
        self.time = time
        self.blood_sugar_level = blood_sugar_level
        self.notes = notes
