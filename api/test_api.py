from fastapi.testclient import TestClient

from config.asgi import app

client = TestClient(app)


def test_posts():
    response = client.get("/api/posts")
    assert response.status_code == 200
    assert response.json() == [{'title': 'First post', 'body': 'This is first post of this project'}]
