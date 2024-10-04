from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Create the Flask SQLAlchemy extension
metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

# Define the Pet model class
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
