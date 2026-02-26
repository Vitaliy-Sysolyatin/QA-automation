from __future__ import annotations

from typing import Any, Dict
from qa_framework.clients.base_client import BaseClient

class ProductsClient(BaseClient):
    def get_product(self, product_id:int) -> Dict[str, Any]:
        resp = self.request("GET", f"/products/{product_id}", expected_status=200)
        return resp.json()