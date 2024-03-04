"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planets, Vehicles
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


@app.route('/character', methods=['GET'])
def handle_get_all_people():

    return jsonify('Hello people!'), 200

@app.route('/character<int:character_id>', methods=['GET','PUT'])
def handle_get_one_character(character_id):
    if request.method == 'GET':
        character1 = Character.query.get(character_id)
        return jsonify(character1.serialize()), 200
    return "Character not found", 404


@app.route('/planets', methods=['GET'])
def handle_get_all_planets():

    return jsonify('We got planets!'), 200


@app.route('/planets<int:planets_id>', methods=['GET','PUT'])
def handle_get_one_planet(planets_id):
    if request.method == 'GET':
        planet1 = Planets.query.get(planets_id)
        return jsonify(planet1.serialize()), 200
    return "Character not found", 404


@app.route('/vehicles', methods=['GET'])
def handle_get_all_vehicles():

    return jsonify('Hi there vehicles!'), 200


@app.route('/vehicles<int:vehicles_id>', methods=['GET','PUT'])
def handle_get_one_vehicle(vehicles_id):
    if request.method == 'GET':
        vehicle1 = Vehicles.query.get(vehicles_id)
        return jsonify(vehicle1.serialize()), 200
    return "Character not found", 404





# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
