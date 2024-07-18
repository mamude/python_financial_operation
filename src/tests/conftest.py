import pytest

from app import create_app, database
from app.models import Account


@pytest.fixture
def app():
    instance_app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})
    with instance_app.app_context():
        database.db.init_app(instance_app)
        database.Base.metadata.create_all(database.db.engine)

        # mock account model
        account = Account(account_number="234", balance="180.37")
        database.db.session.add(account)
        database.db.session.commit()

        yield instance_app


@pytest.fixture
def client(app):
    return app.test_client()

