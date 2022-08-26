"""
Implementation of the :py:class:`abshttp.proto.backend.Backend` protocol using python requests.
"""
from typing import Callable
from typing import Generic
from typing import TypeVar

import requests

from abshttp import proto
from abshttp.response import Response

CallbackReturn = TypeVar("CallbackReturn")


class Backend(proto.Backend[CallbackReturn, CallbackReturn], Generic[CallbackReturn]):
    """
    Implementation of the :py:class:`abshttp.proto.backend.Backend` protocol using python requests.
    """

    def __init__(self, stream=False):
        self._stream = stream

    def _convert_response(self, res: requests.Response) -> proto.Response:
        """ """
        return Response(
            status=res.status_code, headers=list(res.headers.items()), body=res.content
        )

    def send(
        self,
        request: proto.Request,
        callback: Callable[[proto.Request, proto.Response], CallbackReturn],
    ) -> CallbackReturn:
        """ """
        req = requests.Request(
            method=request.method.value.lower(),
            url=request.url.to_string(),
            data=request.body,
            auth=request.auth,
            headers=dict(request.headers),
        ).prepare()

        response = self._convert_response(requests.session().send(req, stream=self._stream))
        return callback(request, response)
