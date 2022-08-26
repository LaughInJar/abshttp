from typing import Protocol


class Response(Protocol):
    """ """

    status: int

    headers: list[tuple[str, str]] = []

    body: bytes = b""
