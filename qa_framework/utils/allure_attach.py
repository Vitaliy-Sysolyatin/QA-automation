from __future__ import annotations

import json
from typing import Any, Mapping, Optional

try:
    import allure
except Exception:
    allure = None


def attach_request(
    *,
    method: str,
    url: str,
    headers: Optional[Mapping[str, Any]] = None,
    params: Optional[Mapping[str, Any]] = None,
    json_body: Any = None,
) -> None:
    if allure is None:
        return

    allure.attach(f"{method} {url}", name="request_line", attachment_type=allure.attachment_type.TEXT)

    if headers:
        allure.attach(
            json.dumps(dict(headers), ensure_ascii=False, indent=2),
            name="request_headers",
            attachment_type=allure.attachment_type.JSON,
        )

    if params:
        allure.attach(
            json.dumps(dict(params), ensure_ascii=False, indent=2),
            name="request_params",
            attachment_type=allure.attachment_type.JSON,
        )

    if json_body is not None:
        allure.attach(
            json.dumps(json_body, ensure_ascii=False, indent=2),
            name="request_json",
            attachment_type=allure.attachment_type.JSON,
        )


def attach_response(*, status_code: int, headers: Mapping[str, Any], body_text: str) -> None:
    if allure is None:
        return

    allure.attach(
        str(status_code),
        name="response_status",
        attachment_type=allure.attachment_type.TEXT,
    )

    if headers:
        allure.attach(
            json.dumps(dict(headers), ensure_ascii=False, indent=2),
            name="response_headers",
            attachment_type=allure.attachment_type.JSON,
        )

    allure.attach(
        body_text[:5000],
        name="response_body",
        attachment_type=allure.attachment_type.TEXT,
    )