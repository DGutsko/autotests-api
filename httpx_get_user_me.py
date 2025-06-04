import httpx

# Авторизация
login_url = "http://localhost:8000/api/v1/authentication/login"
login_data = {
    "email": "daria@example.com",
    "password": "123456"
}

try:
    login_response = httpx.post(login_url, json=login_data)
    login_response.raise_for_status()
    tokens = login_response.json()
    print("Ответ при логине:", tokens)

    # Извлечение токена
    access_token = tokens.get("token", {}).get("accessToken")

    if not access_token:
        raise ValueError("Access token не найден в ответе")

except Exception as e:
    print(f"Ошибка при авторизации: {e}")
    exit(1)

# Получение данных пользователя
user_url = "http://localhost:8000/api/v1/users/me"
headers = {
    "Authorization": f"Bearer {access_token}"
}

try:
    user_response = httpx.get(user_url, headers=headers)
    user_response.raise_for_status()
    print("Статус-код:", user_response.status_code)
    print("JSON-ответ:", user_response.json())

except Exception as e:
    print(f"Ошибка при получении данных пользователя: {e}")
