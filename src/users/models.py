from bson import ObjectId

class User:
    def __init__(self,clerkid, firstname,lastname, email, age, gender, height, weight, medical_conditions, preferences, goals, _id=None):
        self._id = _id if _id is not None else ObjectId()
        self.clerkid = clerkid
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.medical_conditions = medical_conditions
        self.preferences = preferences
        self.goals = goals

    
    
