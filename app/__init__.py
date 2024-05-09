from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize SQLAlchemy with no parameters
db = SQLAlchemy()

class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<QuizResult {self.nickname} scored {self.score}>'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 's8dfgafh2u8euf2e'  
    
    # Database configuration
    URI = os.environ.get('DATABASE_URL', 'sqlite:///default.db')
    if URI.startswith("postgres://"):
        URI = URI.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Import blueprints
    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()  # Create database tables for our data models only once app context is available

    return app
