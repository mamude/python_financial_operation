from dotenv import load_dotenv
from flask import Flask

from app.blueprints import customers
from app.database import db
from app.config import Settings

def create_app(test_config=None) -> Flask:
    load_dotenv()
    config = Settings()

    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
        # configurar conexão com db
        app.config["SQLALCHEMY_DATABASE_URI"] = config.pg_dsn
        db.init_app(app)
    else:
        app.config.from_mapping(test_config)

    # registrar blueprints
    app.register_blueprint(customers.bp)


    return app

if __name__ == "__main__":
    app = create_app()
    app.run()