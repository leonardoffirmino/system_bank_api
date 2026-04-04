from typing import Any, Dict


class HttpRequest:
    def __init__(self, body: Dict[str, Any] | None = None, params: Dict[str, Any] | None = None,
                 headers: Dict[str, Any] | None = None, method: str | None = None,
                 query: Dict[str, Any] | None = None):
        self.body = body or {}
        self.params = params or {}
        self.headers = headers or {}
        self.method = method
        self.query = query or {}
