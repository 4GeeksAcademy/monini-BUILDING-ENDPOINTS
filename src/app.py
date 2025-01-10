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
from models import db, User
from models import db, Planet
from models import db, Vehicle
from models import db, Character



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

@app.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    list_all_users = [user.serialize() for user in all_users]
    return jsonify(list_all_users), 200

@app.route("/user/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    user = user.serialize()
    return jsonify (user), 200

@app.route('/user', methods=['POST'])
def add_user():
   body = request.get_json()
   print(body)
   if "name" not in body:
       return jsonify({
           "msg": "Name shouldn't be empty"}), 400
   if "email" not in body:
       return jsonify({
           "msg": "Email shouldn't be empty"}), 400
   if "password" not in body:
       return jsonify({
           "msg": "Password shouldn't be empty"}), 400
   exist = User.query.filter_by(email = body["email"]).first()
   if exist: 
       return jsonify ({"msg":"User already exists"})
   new_user = User(email = body["email"], name = body["name"], password = body["password"])
   db.session.add(new_user)
   db.session.commit()

   return jsonify({"msg": "User created"}), 200



@app.route('/planets', methods=['GET'])
def get_planets():
    all_planets = Planet.query.all()
    all_planets = list(map(lambda x: x.serialize(), all_planets))
    return jsonify(all_planets), 200

@app.route("/planet/<int:id>", methods=["GET"])
def get_planet(id):
    planet = Planet.query.get(id)
    planet = Planet.serialize()
    return jsonify (planet), 200

@app.route('/planet', methods=['POST'])
def add_planet():
   body = request.get_json()
   print(body)
   if "name" not in body:
       return jsonify({
           "msg": "Name shouldn't be empty"}), 400
   if "population" not in body:
       return jsonify({
           "msg": "Population shouldn't be empty"}), 400
   
   exist = Planet.query.filter_by(name = body["name"]).first()
   if exist: 
       return jsonify ({"msg":"Planet already exists"})
   new_planet = Planet(name = body["name"], population = body["population"])
   db.session.add(new_planet)
   db.session.commit()

   return jsonify({"msg": "Planet created"}), 200



@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    all_vehicles = Vehicle.query.all()
    all_vehicles = list(map(lambda x: x.serialize(), all_vehicles))
    return jsonify(all_vehicles), 200

@app.route("/vehicle/<int:id>", methods=["GET"])
def get_vehicle(id):
    vehicle = Vehicle.query.get(id)
    vehicle = Vehicle.serialize()
    return jsonify (vehicle), 200

@app.route('/vehicle', methods=['POST'])
def add_vehicle():
   body = request.get_json()
   print(body)
   if "type" not in body:
       return jsonify({
           "msg": "Type shouldn't be empty"}), 400
  
   exist = Vehicle.query.filter_by(type = body["type"]).first()
   if exist: 
       return jsonify ({"msg":"Vehicle already exists"})
   new_vehicle = Vehicle(type = body["type"])
   db.session.add(new_vehicle)
   db.session.commit()

   return jsonify({"msg": "Vehicle created"}), 200


@app.route('/characters', methods=['GET'])
def get_characters():
    all_characters = Character.query.all()
    all_characters = list(map(lambda x: x.serialize(), all_characters))
    return jsonify(all_characters), 200

@app.route("/character/<int:id>", methods=["GET"])
def get_character(id):
    character = Character.query.get(id)
    character = Character.serialize()
    return jsonify (character), 200

@app.route('/character', methods=['POST'])
def add_character():
   body = request.get_json()
   print(body)
   if "name" not in body:
       return jsonify({
           "msg": "Name shouldn't be empty"}), 400
   if "gender" not in body:
       return jsonify({
           "msg": "Gender shouldn't be empty"}), 400
   if "age" not in body:
       return jsonify({
           "msg": "Age shouldn't be empty"}), 400
   
   exist = Character.query.filter_by(name = body["name"]).first()
   if exist: 
       return jsonify ({"msg":"Chartacter already exists"})
   new_character = Character(name = body["name"], gender = body ["gender"], afe = body ["age"])
   db.session.add(new_character)
   db.session.commit()

   return jsonify({"msg": "Character created"}), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
