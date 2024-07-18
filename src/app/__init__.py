from dotenv import load_dotenv
from flask import Flask

from app.blueprints import accounts
from app.config import Settings
from app.database import db


def create_app(test_config=None) -> Flask:
    load_dotenv()
    config = Settings()

    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
        # initialize SQLAlchemy
        app.config["SQLALCHEMY_DATABASE_URI"] = config.pg_dsn
        db.init_app(app)
    else:
        app.config.from_mapping(test_config)

    # register blueprints
    app.register_blueprint(accounts.bp)

    return app


if __name__ == "__main__":
    instance_app = create_app()
    instance_app.run()
