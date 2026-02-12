import pytest

from src.clients.base_client import BaseClient


@pytest.mark.smoke
def test_smoke_get_product(api_client: BaseClient) -> None:
    resp = api_client.request("GET", "/products/1", expected_status=200)
    data = resp.json()

    assert data["id"] == 1
    assert "title" in data
