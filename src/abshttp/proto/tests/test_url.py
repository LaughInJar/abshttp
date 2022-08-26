"""
Tests for :py:mod:`abshttp.proto.url`
"""
import dataclasses
from unittest import TestCase

from abshttp.proto.url import URL


class URLFromStringTestCase(TestCase):
    """
    tests for :py:meth:`abshttp.proto.url.URL.from_string

    TODO: use Hypothesis or something?
    """

    def test_simple_http(self):
        """
        test a http URL
        """
        url = "http://example.org"
        result = URL.from_string(url)

        self.assertEqual(
            dataclasses.asdict(result),
            {
                "netloc": "example.org",
                "path": "",
                "fragment": "",
                "username": None,
                "password": None,
                "hostname": "example.org",
                "port": None,
                "scheme": "http",
                "query": {},
            },
        )

        reversed = result.to_string()
        self.assertEqual(url, reversed)

    def test_simple_https(self):
        """
        test a https URL
        """
        url = "https://example.org"
        result = URL.from_string(url)

        self.assertEqual(
            dataclasses.asdict(result),
            {
                "netloc": "example.org",
                "path": "",
                "fragment": "",
                "username": None,
                "password": None,
                "hostname": "example.org",
                "port": None,
                "scheme": "https",
                "query": {},
            },
        )

        reversed = result.to_string()
        self.assertEqual(url, reversed)

    def test_auth(self):
        """
        test a URL with user + password
        """
        url = "https://user:password@example.org"
        result = URL.from_string(url)

        self.assertEqual(
            dataclasses.asdict(result),
            {
                "netloc": "user:password@example.org",
                "path": "",
                "fragment": "",
                "username": "user",
                "password": "password",
                "hostname": "example.org",
                "port": None,
                "scheme": "https",
                "query": {},
            },
        )

        reversed = result.to_string()
        self.assertEqual(url, reversed)

    def test_user(self):
        """
        test a URL with a user
        """
        url = "https://user@example.org"
        result = URL.from_string(url)

        self.assertEqual(
            dataclasses.asdict(result),
            {
                "netloc": "user@example.org",
                "path": "",
                "fragment": "",
                "username": "user",
                "password": None,
                "hostname": "example.org",
                "port": None,
                "scheme": "https",
                "query": {},
            },
        )

        reversed = result.to_string()
        self.assertEqual(url, reversed)

    def test_fragment(self):
        """
        test a URL with a fragment
        """
        url = "https://example.org#frag"
        result = URL.from_string(url)

        self.assertEqual(
            dataclasses.asdict(result),
            {
                "netloc": "example.org",
                "path": "",
                "fragment": "frag",
                "username": None,
                "password": None,
                "hostname": "example.org",
                "port": None,
                "scheme": "https",
                "query": {},
            },
        )

        reversed = result.to_string()
        self.assertEqual(url, reversed)

    def test_path(self):
        """
        test a URL with a path
        """
        url = "https://example.org/path/to/file.html"
        result = URL.from_string(url)

        self.assertEqual(
            dataclasses.asdict(result),
            {
                "netloc": "example.org",
                "path": "/path/to/file.html",
                "fragment": "",
                "username": None,
                "password": None,
                "hostname": "example.org",
                "port": None,
                "scheme": "https",
                "query": {},
            },
        )

        reversed = result.to_string()
        self.assertEqual(url, reversed)

    def test_port(self):
        """
        test a URL with a port
        """
        url = "https://example.org:8080"
        result = URL.from_string(url)

        self.assertEqual(
            dataclasses.asdict(result),
            {
                "netloc": "example.org:8080",
                "path": "",
                "fragment": "",
                "username": None,
                "password": None,
                "hostname": "example.org",
                "port": 8080,
                "scheme": "https",
                "query": {},
            },
        )

        reversed = result.to_string()
        self.assertEqual(url, reversed)

    def test_query_param(self):
        """
        test a single query param
        """
        url = "https://example.org?key=value"
        result = URL.from_string(url)

        self.assertEqual(
            dataclasses.asdict(result),
            {
                "netloc": "example.org",
                "path": "",
                "fragment": "",
                "username": None,
                "password": None,
                "hostname": "example.org",
                "port": None,
                "scheme": "https",
                "query": {"key": ["value"]},
            },
        )

        reversed = result.to_string()
        self.assertEqual(url, reversed)

    def test_query_params(self):
        """
        test 2 query params
        """
        url = "https://example.org?key=value&key2=value2"
        result = URL.from_string(url)

        self.assertEqual(
            dataclasses.asdict(result),
            {
                "netloc": "example.org",
                "path": "",
                "fragment": "",
                "username": None,
                "password": None,
                "hostname": "example.org",
                "port": None,
                "scheme": "https",
                "query": {"key": ["value"], "key2": ["value2"]},
            },
        )

    def test_query_param_repeat(self):
        """
        test what happens when the same query param is repeated
        """
        url = "https://example.org?key=value&key=value2"
        result = URL.from_string(url)

        self.assertEqual(
            dataclasses.asdict(result),
            {
                "netloc": "example.org",
                "path": "",
                "fragment": "",
                "username": None,
                "password": None,
                "hostname": "example.org",
                "port": None,
                "scheme": "https",
                "query": {"key": ["value", "value2"]},
            },
        )

    def test_full(self):
        """
        test parsing of a url with everything
        """
        url = "https://user:password@example.org:8080/path/to/file.html?key=value&key=value2&key2=value3#anchor"
        result = URL.from_string(url)

        self.assertEqual(
            dataclasses.asdict(result),
            {
                "netloc": "user:password@example.org:8080",
                "path": "/path/to/file.html",
                "fragment": "anchor",
                "username": "user",
                "password": "password",
                "hostname": "example.org",
                "port": 8080,
                "scheme": "https",
                "query": {"key": ["value", "value2"], "key2": ["value3"]},
            },
        )
