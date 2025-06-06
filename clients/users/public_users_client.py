from typing import TypedDict
from httpx import Response

from clients.api_client import APIClient


class CreateUserRequest(TypedDict):
    """
    Структура данных для создания пользователя.

    Attributes:
        username (str): Имя пользователя.
        email (str): Адрес электронной почты.
        password (str): Пароль пользователя.
    """
    username: str
    email: str
    password: str


class PublicUsersClient(APIClient):
    """
    API-клиент для публичных пользовательских эндпоинтов (не требует авторизации).
    """

    def create_user_api(self, request: CreateUserRequest) -> Response:
        """
        Отправляет POST-запрос к /api/v1/users для создания нового пользователя.

        Args:
            request (CreateUserRequest): Данные пользователя для создания, включая имя, email и пароль.

        Returns:
            Response: Ответ от сервера (httpx.Response), содержащий результат создания.
        """
        return self.post("/api/v1/users", json=request)