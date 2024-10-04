from flask import Flask
from flask_migrate import Migrate
from models import db

# Create a Flask application object
app = Flask(__name__)

# Configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# Initialize the Flask application to use the database
db.init_app(app)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
