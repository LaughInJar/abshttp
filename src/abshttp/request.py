"""
Implement the request protocol
"""
from enum import Enum
from typing import Iterable

from . import proto
from .proto.request import Method
from .proto.url import URL


class Request(proto.Request):
    """
    Implementation of the :py:class:`abshttp.proto.request.Request` protocol
    """

    def __init__(
        self,
        url: str,
        method: Method = Method.GET,
        body: bytes = None,
        params: dict[str, str] = {},
        headers: list[tuple[str, str]] = [],
        auth: tuple[str, str] = None,
    ):
        """ """
        self.headers = headers
        self.url = URL.from_string(url)
        self._merge_params(params),
        self.auth = auth
        self.method = method
        self.body = body

    def _merge_params(self, params: dict[str, str] = {}):
        """merge the query params from the given url-string with the explicit query params given."""
        for key, value in params.items():
            self.url.query.setdefault(key, []).append(value)
