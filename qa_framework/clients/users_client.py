from __future__ import annotations

from typing import Any, Dict
from qa_framework.clients.base_client import BaseClient

class UsersClient(BaseClient):
    def get_user(self, user_id:int) -> Dict[str, Any]:
        resp = self.request("GET", f"/users/{user_id}", expected_status=200)
        return resp.json()
    
    def list_users(self, *, limit: int = 30, skip: int = 0) -> Dict[str, Any]:
        resp = self.request(
            "GET", 
            "/users", 
            params={"limit": limit, "skip": skip}, 
            expected_status=200
            )
        return resp.json()