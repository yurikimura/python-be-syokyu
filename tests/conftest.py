import pytest

from app.database import SessionLocal
from app.models import item_model, list_model


@pytest.fixture(autouse=False)
def db_session():
    db = SessionLocal()
    try:
        db.query(list_model.ListModel).delete()
        db.query(item_model.ItemModel).delete()
        db.commit()
        yield db
    finally:
        db.query(list_model.ListModel).delete()
        db.query(item_model.ItemModel).delete()
        db.commit()
        db.close()
