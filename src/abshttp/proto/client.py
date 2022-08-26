"""
Protocol for a basic http client abstraction
"""
import typing
from typing import Protocol
from typing import TypeVar

from abshttp.proto.request import Request
from abshttp.proto.response import Response

CallbackReturn = TypeVar("CallbackReturn", covariant=True)
BackendReturn = TypeVar("BackendReturn", covariant=True)


class Client(Protocol[BackendReturn, CallbackReturn]):
    """ """

    def callback(self, request: Request, response: Response) -> CallbackReturn:
        ...

    def send(self, request: Request) -> BackendReturn:
        """ """
        ...

    # TODO: add convenience methods like this for GET, POST, PUT, HEAD, OPTIONS, DELETE
    # def get(self, url: str, params: dict, auth: tuple, ...):
