import pytest

from app.database import SessionLocal
from app.models import item_model, list_model


@pytest.fixture
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(autouse=True)
def db_clear_all(db_session):
    db_session.query(list_model.ListModel).delete()
    db_session.query(item_model.ItemModel).delete()
    db_session.commit()
    yield
    db_session.query(list_model.ListModel).delete()
    db_session.query(item_model.ItemModel).delete()
    db_session.commit()
