from __future__ import annotations

from typing import Any, Mapping, Optional

import httpx


class ApiError(RuntimeError):
    """Raised when API returns unexpected status code."""


class BaseClient:
    def __init__(
        self,
        base_url: str,
        *,
        timeout_seconds: float = 10,
        headers: Optional[Mapping[str, str]] = None,
    ) -> None:
        self._client = httpx.Client(
            base_url=base_url,
            timeout=httpx.Timeout(timeout_seconds),
            headers=headers,
            follow_redirects=True,
        )

    def close(self) -> None:
        self._client.close()

    def request(
        self,
        method: str,
        url: str,
        *,
        params: Optional[Mapping[str, Any]] = None,
        json: Any = None,
        expected_status: int | tuple[int, ...] = (200,),
    ) -> httpx.Response:
        resp = self._client.request(method, url, params=params, json=json)

        ok = (expected_status,) if isinstance(expected_status, int) else expected_status
        if resp.status_code not in ok:
            raise ApiError(
                f"Unexpected status {resp.status_code} for {method} {url}. "
                f"Expected {ok}. Body: {resp.text[:500]}"
            )
        return resp