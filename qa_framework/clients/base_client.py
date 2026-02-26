import httpx

from typing import Any, Mapping, Optional
from qa_framework.utils.allure_attach import attach_request, attach_response


class ApiError(RuntimeError):
    pass


class BaseClient:
    def __init__(self, base_url: str, *, timeout_seconds: float = 10,
                 headers: Optional[Mapping[str, str]] = None) -> None:
        self._client = httpx.Client(
            base_url=base_url,
            timeout=httpx.Timeout(timeout_seconds),
            headers=headers,
            follow_redirects=True,
        )

    def close(self) -> None:
        self._client.close()

    def request(self, method: str, url: str, *, params=None, json=None,
                expected_status: int | tuple[int, ...] = (200,)) -> httpx.Response:
        attach_request(method=method, url=url, headers=self._client.headers, params=params, json_body=json)
        
        resp = self._client.request(method, url, params=params, json=json)
        
        attach_response(status_code=resp.status_code, headers=resp.headers, body_text=resp.text)
        
        ok = (expected_status,) if isinstance(expected_status, int) else expected_status
        if resp.status_code not in ok:
            raise ApiError(
                f"Unexpected status {resp.status_code} for {method} {url}. "
                f"Expected {ok}. Body: {resp.text[:500]}"
            )
        return resp
