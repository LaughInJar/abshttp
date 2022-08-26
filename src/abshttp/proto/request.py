from typing import Protocol

from abshttp.proto.url import URL


class Request(Protocol):
    """ """

    url: URL

    auth: tuple[str, str]

    headers: list[tuple[str, str]]
