import pytest

from qa_framework.clients.users_client import UsersClient

class TestUsers:
    def test_list_users_returns_expected_shape(self, users_client: UsersClient) -> None:
        data = users_client.list_users(limit=10, skip=0)

        assert isinstance(data, dict)

        assert "users" in data
        assert "total" in data
        assert "limit" in data
        assert "skip" in data

        users = data["users"]
        assert isinstance(users, list)
        assert len(users) <= 10

        if users:
            first = users[0]
            assert isinstance(first, dict)
            assert "id" in first
            assert "username" in first

    def test_list_users_pagination_has_no_overlap(self, users_client: UsersClient) -> None:
        page1 = users_client.list_users(limit=5, skip=0)
        page2 = users_client.list_users(limit=5, skip=5)

        users1 = page1["users"]
        users2 = page2["users"]

        assert users1
        assert users2

        ids1 = {u["id"] for u in users1}
        ids2 = {u["id"] for u in users2}
        assert "id" in users1[0]
        assert "id" in users2[0]

        assert ids1.isdisjoint(ids2)

    def test_list_users_invalid_limit_is_normalized(self, users_client: UsersClient) -> None:
        data = users_client.list_users(limit=-1, skip=0)

        assert isinstance(data, dict)

        assert "users" in data
        assert "total" in data
        assert "limit" in data
        assert "skip" in data
        
        users = data["users"]
        limit = data["limit"]
        total = data["total"]

        assert isinstance(limit, int)
        assert isinstance(total, int)

        assert limit > 0
        assert limit <= total
        assert len(users) <= limit
        assert limit != -1
