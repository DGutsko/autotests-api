import httpx
from tools.fakers import get_random_email


# Создание пользователя
create_user_url = "http://localhost:8000/api/v1/users"
user_email = get_random_email()

user_data = {
    "email": user_email,
    "password": "123456",
    "firstName": "Daria",
    "lastName": "Ivanova",
    "middleName": "Sergeevna"
}

try:
    create_response = httpx.post(create_user_url, json=user_data)
    print(f"Статус-код при создании: {create_response.status_code}")
    create_response.raise_for_status()
    created_user = create_response.json()
    user_id = created_user.get("user", {}).get("id")
    print(f"Создан пользователь с ID: {user_id}")

except Exception as e:
    print(f"Ошибка при создании пользователя: {e}")
    exit(1)


# Авторизация созданного пользователя
login_url = "http://localhost:8000/api/v1/authentication/login"
login_data = {
    "email": user_email,
    "password": user_data["password"]
}

try:
    login_response = httpx.post(login_url, json=login_data)
    print(f"Статус-код при авторизации: {login_response.status_code}")
    login_response.raise_for_status()
    tokens = login_response.json()
    access_token = tokens.get("token", {}).get("accessToken")
    if not access_token:
        raise ValueError("Не найден accessToken")
    print("Авторизация прошла успешно")
except Exception as e:
    print(f"Ошибка при авторизации: {e}")
    exit(1)


# Обновление пользователя через PATCH
update_url = f"http://localhost:8000/api/v1/users/{user_id}"
headers = {
    "Authorization": f"Bearer {access_token}"
}
update_data = {
    "email": get_random_email(),
    "firstName": "Anna",
    "lastName": "Petrova",
    "middleName": "Sergeevna"
}

try:
    patch_response = httpx.patch(update_url, headers=headers, json=update_data)
    print(f"Статус-код при обновлении: {patch_response.status_code}")
    patch_response.raise_for_status()
    print("Пользователь успешно обновлён.")
    print("Ответ:", patch_response.json())
except Exception as e:
    print(f"Ошибка при обновлении пользователя: {e}")
    exit(1)

