import pytest

from collections.abc import Iterator
from src.clients.base_client import BaseClient
from src.config.settings import settings


@pytest.fixture(scope="session")
def api_client() -> Iterator[BaseClient]:
    client = BaseClient(
        base_url=settings.base_url,
        timeout_seconds=settings.timeout_seconds,
    )
    yield client
    client.close()
