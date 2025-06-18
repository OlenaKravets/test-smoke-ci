import requests

def test_get_posts():
    """🟢 Перевірка GET-запиту: отримаємо список постів"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "title" in response.json()[0]

def test_create_post():
    """🟡 Перевірка POST-запиту: створення нового посту"""
    payload = {
        "title": "Test Post",
        "body": "Це тіло тестового посту",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

