from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# TODO: Station00 を Station 01 になるよう各 Station 番号を調整する。
def test_first_test():
    """Station00合格判定テストコード."""
    response = client.get("/hello")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"Message": "Hello FastAPI!"}
