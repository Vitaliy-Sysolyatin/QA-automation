import pytest
import os

from collections.abc import Iterator
from qa_framework.clients.base_client import BaseClient
from qa_framework.config.settings import settings
from qa_framework.clients.auth_client import AuthClient
from qa_framework.clients.products_client import ProductsClient
from qa_framework.clients.users_client import UsersClient


@pytest.fixture(scope="session")
def api_client() -> Iterator[BaseClient]:
    client = BaseClient(
        base_url=settings.base_url,
        timeout_seconds=settings.timeout_seconds,
    )
    yield client
    client.close()

@pytest.fixture(scope="session")
def auth_client() -> Iterator[AuthClient]:
    client = AuthClient(base_url=settings.base_url, timeout_seconds=settings.timeout_seconds)
    yield client
    client.close()

@pytest.fixture(scope="session")
def demo_credentials() -> tuple[str, str]:
    username = os.getenv("DUMMYJSON_USERNAME", "emilys")
    password = os.getenv("DUMMYJSON_PASSWORD", "emilyspass")
    return username, password

@pytest.fixture(scope="session")
def products_client() -> Iterator[ProductsClient]:
    client = ProductsClient(
        base_url=settings.base_url,
        timeout_seconds=settings.timeout_seconds
    )
    yield client
    client.close()

@pytest.fixture(scope="session")
def users_client() -> Iterator[UsersClient]:
    client = UsersClient(
        base_url=settings.base_url,
        timeout_seconds=settings.timeout_seconds
    )
    yield client
    client.close()

