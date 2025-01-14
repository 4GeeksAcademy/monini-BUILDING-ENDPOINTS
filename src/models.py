from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String (30), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    character_favorites = db.relationship("Character_Favorites", backref = "user")
    vehicle_favorites = db.relationship("Vehicle_Favorites", backref = "user")
    planet_favorites = db.relationship("Planet_Favorites", backref = "user")
    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "Character_Favorites": [fav.serialize() for fav in self.character_favorites],
            "Vehicle_Favorites": [fav.serialize() for fav in self.vehicle_favorites],
            "Planet_Favorites": [fav.serialize() for fav in self.planet_favorites]
            # do not serialize the password, its a security breach
        }
    
class Planet(db.Model):

    __tablename__ = "planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String (30), unique=False, nullable=True)
    population = db.Column(db.Integer, nullable=True)

        
    def __repr__(self):
        return '<planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            
        }
    

class Planet_Favorites(db.Model):

     __tablename__ = "planet favorites"
     id = db.Column(db.Integer, primary_key=True)
     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
     Planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
     planets = db.relationship("Planet", backref = "planet_favorites")
        
     def __repr__(self):
        return '<planet %r>' % self.id

     def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id":self.planet_id,
            "planet":self.planet.serialize() if self.planets else None
            # do not serialize the password, its a security breach
        }


class Character(db.Model):

    __tablename__ = "character"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String (30), unique=False, nullable=True)
    gender = db.Column(db.String (15), unique=False, nullable=True)
    age = db.Column(db.String (15), unique=False, nullable=True)

    def __repr__(self):
        return '<character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "age": self.age,

            # do not serialize the password, its a security breach
        }
    
class Character_Favorites(db.Model):

    __tablename__ = "character favorites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    characters = db.relationship("Character", backref = "character_favorites")
        
    def __repr__(self):
        return '<character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id":self.character_id,
            "characters":self.characters.serialize() if self.characters else None
            # do not serialize the password, its a security breach
        }
    
class Vehicle(db.Model):

    __tablename__ = "vehicle"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String (30), unique=False, nullable=True)


    def __repr__(self):
        return '<vehicle %r>' % self.type

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type
            # do not serialize the password, its a security breach
        }

class Vehicle_Favorites(db.Model):

     __tablename__ = "vehicle favorites"
     id = db.Column(db.Integer, primary_key=True)
     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
     vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"))
     vehicles = db.relationship("Vehicle", backref = "vehicle_favorites")
        
     def __repr__(self):
        return '<vehicle %r>' % self.id

     def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vehicle_id":self.character_id,
            "vehicles":self.vehicles.serialize() if self.vehicles else None
            # do not serialize the password, its a security breach
        }