from dataclasses import dataclass
from dataclasses import field
from typing import Optional
from urllib.parse import parse_qs
from urllib.parse import urlencode
from urllib.parse import urlparse
from urllib.parse import urlunparse


@dataclass
class URL:
    """Representation of an URL. Based on the named tuple that :py:meth:`urllib.parse.urlparse` returns.

    Basically, this is just a mutable version of the "ParseResult" named tuple.
    """

    @classmethod
    def from_string(cls, url: str) -> "URL":
        """create a :py:class:`URL` dataclass from the given URL in string-form

        :param url: the url as string form
        :return: the URL object
        """
        parse_result = urlparse(url, scheme="https")
        return URL(
            netloc=parse_result.netloc,
            path=parse_result.path,
            fragment=parse_result.fragment,
            username=parse_result.username,
            password=parse_result.password,
            hostname=parse_result.hostname,
            port=parse_result.port,
            scheme=parse_result.scheme,
            query=parse_qs(parse_result.query),
        )

    def to_string(self) -> str:
        """construct a string repesentation of this URL object"""
        query = urlencode(self.query, doseq=True)
        return urlunparse((self.scheme, self.netloc, self.path, "", query, self.fragment))

    #: hostname plus optional port (e.g. localhost:8080)
    netloc: str

    #: path portion of the urlURL
    path: str

    #: the fragment (the stuff after the # in the URL which usually isn't sent to the server)
    fragment: str

    #: some urls contain the username in the url like so https://user@hostname/path/
    username: Optional[str] = None

    #: some urls contain the username + password in the url like so https://user:pass@hostname/path/
    password: Optional[str] = None

    #: the hostname without the port
    hostname: Optional[str] = None

    #: the port
    port: Optional[int] = None

    #: http, https, ftp, etc.
    scheme: str = "https"

    #: the query string as dictionary (see urllib.parse.parse_qs)
    query: dict[str, list[str]] = field(default_factory=dict)
