import requests

def test_all_posts_data_structure():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # 1. Статус код
    assert response.status_code == 200, "❌ Очікували статус 200"

    posts = response.json()

    # 2. Кількість постів
    assert len(posts) == 100, f"❌ Очікували 100 постів, отримали {len(posts)}"

    # 3. Структура кожного поста
    for post in posts:
        assert "userId" in post, "❌ Відсутнє поле 'userId'"
        assert "id" in post, "❌ Відсутнє поле 'id'"
        assert "title" in post, "❌ Відсутнє поле 'title'"
        assert "body" in post, "❌ Відсутнє поле 'body'"
