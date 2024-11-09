""" Requests Wrapper Object """

import logging
from json import JSONDecodeError

import requests
from requests import request
from urllib3.util import Url

from PetStore.lib.constants.constant import Constants as Const

logging.basicConfig(level=logging.DEBUG)


class BaseApiObject(object):
    """ Base API Object """

    _status_code = None
    _request_headers = None
    _response_headers = None
    _text = None
    _response = None
    _hostname = None

    def __init__(self, app_url: str = None):
        app_url = Const.DEFAULT_BASE_API_URL if app_url is None else app_url

        self._session = requests.Session()
        self._session_access = None
        self._session_headers = {}
        self._session_url = app_url

        # url = Url(app_url)
        # self._hostname = url.hostname

    @property
    def http_text(self) -> str:
        """ Returns the HTTP Response Text """
        return self._text

    @property
    def http_status_code(self) -> int:
        """ Returns the HTTP Status Code """
        return self._status_code

    @property
    def http_request_headers(self) -> dict:
        """ Returns the HTTP request headers """
        return self._request_headers

    @property
    def http_response_headers(self) -> dict:
        """ Returns the HTTP response headers """
        return self._response_headers

    @property
    def session_headers(self) -> dict:
        """ Returns session headers """
        return self._session_headers

    @session_headers.setter
    def session_headers(self, headers: dict):
        """
        Sets session headers

        :param dict headers: A dictionary containing headers
        """
        self._session_headers = headers

    @property
    def session_url(self) -> str:
        """ Returns session URL """
        return self._session_url

    @session_url.setter
    def session_url(self, value: str):
        """
        Sets URL for session

        :param str value: URL for session
        """
        self._session_url = value

    @property
    def response(self) -> requests.Response:
        """ Returns the last response """
        return self._response

    @property
    def request_session(self) -> requests.Session:
        """ Returns the session """
        return self._session

    def add_header(self, header: dict) -> None:
        """
        Adds a header to session headers

        :param dict header: A dictionary containing one or more headers to inject into existing session headers
        """
        self._session_headers.update(header)

    def remove_header(self, key: str) -> None:
        """
        Deletes a header from session headers

        :param str key: Header to delete from headers dictionary
        :returns: None if key is not present in headers dictionary
        """
        if key not in self._session_headers:
            return None
        self._session_headers.pop(key)

    def request(self, method: str, route: str, params=None, **kwargs):
        """
        Wrapper method for sending HTTP requests

        :param str method: HTTP Method (i.e. GET, POST, PATCH, ...)
        :param str route: API route
        :param params: Query parameters of API routes
        :param dict kwargs: Keyword arguments, supports same kwargs as Python's requests library
        :returns: API response (JSON, File Contents, Text, ...)
        :raises: HTTPError
        """
        expected_headers = self.session_headers

        expected_content_type = 'application/x-www-form-urlencoded' if 'login' in route else 'application/json'
        expected_headers["Content-Type"] = expected_content_type
        expected_headers["Accept"] = 'application/json'

        if method.lower() not in Const.HTTPMethods.VALID_METHODS:
            raise Exception('Invalid HTTP method "{}"'.format(method))

        # if kwargs:
        #     _kwargs = self._build_request_kwargs(**kwargs)
        #     expected_payload_keyword = 'data' if 'login' in route else 'json'
        #
        #     if _kwargs.get(expected_payload_keyword):
        #         logging.debug('Sending data :: {}'.format(kwargs.get(expected_payload_keyword)))

        url = self._session_url + "/v2" + route
        response = request(method=method, url=url, params=params, **kwargs)
        self._response = response

        # if not _kwargs['stream']:
        #     self._text = response.text

        self._status_code = response.status_code
        self._request_headers = response.request.headers
        self._response_headers = response.headers
        # response.raise_for_status()

        return response

    def _build_request_kwargs(self, **kwargs):
        kwargs.setdefault('data', None)
        kwargs.setdefault('json', None)
        kwargs.setdefault('headers', self.session_headers)
        kwargs.setdefault('stream', None)

        _kwargs = {'headers': kwargs['headers'], 'data': kwargs['data'], 'json': kwargs['json'],
                   'stream': kwargs['stream']}

        return _kwargs


class ResponseObject(dict):
    """ API Response Object """

    def __new__(cls, response):
        response_dict = {}

        if isinstance(getattr(response, 'json', {}), dict):
            return {}

        try:
            if response.json() is None:
                return {}
            response_dict = response.json()
        except JSONDecodeError:
            if not response.text:
                return {}
        finally:
            return response_dict
