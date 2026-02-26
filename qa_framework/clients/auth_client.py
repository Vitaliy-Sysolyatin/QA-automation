from typing import Any, Dict
from qa_framework.clients.base_client import BaseClient


class AuthClient(BaseClient):
    def login(self, username: str, password: str) -> Dict[str, Any]:
        payload = {"username": username, "password": password}
        resp = self.request("POST", "/auth/login", json=payload, expected_status=(200))
        return resp.json()
