def test_ui_login_title():
    # Це умовна перевірка UI
    page_title = "Login | MyApp"
    assert "Login" in page_title, "❌ Заголовок не містить 'Login'"
