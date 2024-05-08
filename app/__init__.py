from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main)
    app.secret_key = 's8dfgafh2u8euf2e'

    return app
