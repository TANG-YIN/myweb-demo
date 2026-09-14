from flask import Flask
from .config import Config
from .db import close_db
from .users.routes import bp as users_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.teardown_appcontext(close_db)

    app.register_blueprint(users_bp, url_prefix="/users")

    return app
