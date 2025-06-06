from httpx import Client
from clients.users.public_users_client import PublicUsersClient

if __name__ == "__main__":
    client = Client(base_url="http://localhost:8000")
    users_client = PublicUsersClient(client)

    new_user_data = {
        "username": "testuser1",
        "email": "testuser1@example.com",
        "password": "supersecret",
        "firstName": "Тест",
        "lastName": "Пользователь",
        "middleName": "Отчество"
    }

    response = users_client.create_user_api(new_user_data)

    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except Exception as e:
        print("Ошибка при чтении JSON:", str(e))

    client.close()