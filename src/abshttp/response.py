from . import proto


class Response(proto.Response):
    """
    Implementation of the :py:class:`abshttp.proto.request.Request` protocol
    """

    def __init__(self, status: int, headers: list[tuple[str, str]] = [], body: bytes = b""):
        """ """
        self.headers = headers
        self.status = status
        self.body = body
