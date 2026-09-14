from flask import Flask
from .config import Config
from .db import get_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.teardown_appcontext(close_db)

    from .users.routes import bp as users_bp
    app.register_blueprint(users_bp)

    return app
