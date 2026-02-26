from __future__ import annotations
from typing import Any, Mapping

def extract_token(payload: Mapping[str, Any]) ->str:

    token = payload.get("accessToken") or payload.get("token")
    if not token or not isinstance(token, str):
        raise AssertionError(f'Token field not found in response. Keys: {list(payload.keys())}')
    return token