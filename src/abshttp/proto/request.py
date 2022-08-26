from enum import Enum
from typing import Optional
from typing import Protocol

from abshttp.proto.url import URL


class Method(Enum):
    """Http request methods"""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    CONNECT = "CONNECT"
    TRACE = "TRACE"
    PATCH = "PATCH"


class Request(Protocol):
    """Representation of a http request method"""

    url: URL

    method: Method = Method.GET

    auth: Optional[tuple[str, str]]

    headers: list[tuple[str, str]] = []

    body: Optional[bytes] = None
