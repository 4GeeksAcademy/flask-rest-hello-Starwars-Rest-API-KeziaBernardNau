from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    user_name = db.Column(db.String(120), unique=True, nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "user_name": self.user_name
        }
    
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    climate = db.Column(db.String(120), unique=True, nullable=False)
    diameter = db.Column(db.String(80), unique=False, nullable=False)
    gravity = db.Column(db.String(80), unique=False, nullable=False)
    planet_name = db.Column(db.String(120), unique=True, nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "climate": self.climate,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "planet_name": self.planet_name
        }
    

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    birth_year = db.Column(db.String(120), unique=True, nullable=False)
    eye_color = db.Column(db.String(80), unique=False, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    character_name = db.Column(db.String(120), unique=True, nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "character_name": self.character_name
        }
    
class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cargo_capacity = db.Column(db.String(120), unique=True, nullable=False)
    consumables = db.Column(db.String(80), unique=False, nullable=False)
    cost_in_credits = db.Column(db.String(80), unique=False, nullable=False)
    vehicles_name = db.Column(db.String(120), unique=True, nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "cost_in_credits": self.cost_in_credits,
            "vehicles_name": self.vehicles_name
        }
    

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, ForeignKey('character.id'), nullable=True)
    vehicles_id = db.Column(db.Integer, ForeignKey('vehicles.id'), nullable=True)
    planets_id = db.Column(db.Integer, ForeignKey('planets.id'), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "vehicles_id": self.vehicles_id,
            "planets_id": self.planets_id
        }