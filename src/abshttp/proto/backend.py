"""
Protocol for http client backends
"""
from typing import Callable
from typing import Protocol
from typing import TypeVar

from abshttp.proto.request import Request
from abshttp.proto.response import Response

CallbackReturn = TypeVar("CallbackReturn", contravariant=True)
BackendReturn = TypeVar("BackendReturn", covariant=True)


class Backend(Protocol[BackendReturn, CallbackReturn]):
    """ """

    def send(
        self, request: Request, callback: Callable[[Request, Response], CallbackReturn]
    ) -> BackendReturn:
        """ """
        ...
