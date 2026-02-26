import pytest

from qa_framework.clients.auth_client import AuthClient
from qa_framework.utils.validators import extract_token


def test_login_success(auth_client: AuthClient, demo_credentials: tuple[str, str]) -> None:
    username, password = demo_credentials
    data = auth_client.login(username=username, password=password)

    token = extract_token(data)
    assert token
    assert data.get("username") == username

@pytest.mark.smoke
@pytest.mark.parametrize(
    ("username", "password"),
    [
        ("kminchelle", "wrong_password"),
        ("wrong_user", "0lelplR"),
        ("", ""),
    ],
)
def test_login_negative(auth_client: AuthClient, username: str, password: str) -> None:
    resp = auth_client.request(
        "POST",
        "/auth/login",
        json={"username": username, "password": password},
        expected_status=(400, 401),
    )
    assert resp.status_code in (400, 401)