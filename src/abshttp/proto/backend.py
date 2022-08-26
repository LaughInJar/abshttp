from typing import Protocol
from typing import TypeVar

ClientReturn = TypeVar("ClientReturn", covariant=True)


class Backend(Protocol[ClientReturn]):
    """ """
