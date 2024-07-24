# Setup db inside the __init__.py under project folder
from adoption_site import db

class Puppy(db.Model):
    __tablename__ = "puppies"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db. Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Puppy ID: {self.id}, puppy name: {self.name}"
    

class Owner(db.Model):
    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db. Text)
    pup_id = db.Column(db.Integer, db.ForeignKey("puppies.id"))

    def __init__(self, name, pup_id):
        self.name = name
        self.pup_id = pup_id

    def __repr__(self):
        return f"Owner name: {self.name} and pup id:{self.pup_id}"