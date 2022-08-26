import json
from typing import Any
from typing import Generic

from abshttp.proto.backend import BackendReturn
from abshttp.proto.client import CallbackReturn

from . import proto


class BaseClient(
    proto.Client[BackendReturn, CallbackReturn],
    Generic[BackendReturn, CallbackReturn],
):
    """ """

    def __init__(self, backend: proto.Backend[BackendReturn, Any]):
        self.backend = backend

    def callback(self, request: proto.Request, response: proto.Response) -> CallbackReturn:
        """ """
        raise NotImplemented

    def send(self, request: proto.Request) -> BackendReturn:
        """ """
        return self.backend.send(request, self.callback)


class JsonClient(BaseClient[BackendReturn, Any], Generic[BackendReturn]):
    """
    Client that parses the response as JSON

    .. code-block:: python

        from abshttp.backend import requests
        from abshttp.client import JsonClient
        from abshttp.request import Request


        URL = "https://en.wikipedia.org/w/api.php"

        SEARCHPAGE = "Nelson Mandela"

        PARAMS = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": SEARCHPAGE
        }

        client = JsonClient(backend=requests.Backend())
        response = client.send(Request(url="https://en.wikipedia.org/w/api.php", params=PARAMS))

        print(response)

    """

    def __init__(self, backend: proto.Backend[BackendReturn, Any]):
        self.backend = backend

    def callback(self, request: proto.Request, response: proto.Response) -> Any:
        encoding = "utf-8"  # TODO: determine encoding from response headers
        return json.loads(response.body.decode(encoding))
