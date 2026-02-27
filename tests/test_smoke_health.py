import pytest

from qa_framework.clients.products_client import ProductsClient


@pytest.mark.smoke
def test_smoke_get_product(products_client: ProductsClient) -> None:
    data = products_client.get_product(1)
    assert data["id"] == 1
    assert "title" in data
