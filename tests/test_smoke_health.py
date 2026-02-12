import httpx

BASE_URL = "https://dummyjson.com"

def test_smoke_get_product():
    r = httpx.get(f"{BASE_URL}/products/1", timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == 1
    assert "title" in data
