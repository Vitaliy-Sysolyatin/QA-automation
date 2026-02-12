from __future__ import annotations

import os
from dataclasses import dataclass


def _get_env(name: str, default: str) -> str:
    value = os.getenv(name)
    return value.strip() if value else default


@dataclass(frozen=True)
class Settings:
    base_url: str = _get_env("BASE_URL", "https://dummyjson.com")
    timeout_seconds: float = float(_get_env("HTTP_TIMEOUT", "10"))


settings = Settings()