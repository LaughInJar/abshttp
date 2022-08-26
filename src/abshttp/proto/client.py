"""
Protocol for a basic http client abstraction
"""
from typing import Callable
from typing import Protocol
from typing import TypeVar

from abshttp.proto.backend import Backend
from abshttp.proto.backend import ClientReturn
from abshttp.proto.request import Request
from abshttp.proto.response import Response

CallbackReturn = TypeVar("CallbackReturn", covariant=True)
HttpBackend = TypeVar("HttpBackend", bound=Backend, covariant=True)


class Client(Protocol[HttpBackend, ClientReturn]):
    """ """

    def send(
        self, request: Request, callback: Callable[[Response], CallbackReturn]
    ) -> ClientReturn:
        """ """
        ...

    # TODO: add convenience methods like this for GET, POST, PUT, HEAD, OPTIONS, DELETE
    # def get(self, url: str, params: dict, auth: tuple, ...):
