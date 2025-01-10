from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String (30), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorite = db.relationship("Favorites", backref = "user")

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name
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

class Vehicle(db.Model):

    __tablename__ = "vehicle"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String (30), unique=False, nullable=True)


    def __repr__(self):
        return '<vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type
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
    
class Favorites(db.Model):

    __tablename__ = "favorites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

        
    def __repr__(self):
        return '<vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id
            
            # do not serialize the password, its a security breach
        }
    
    