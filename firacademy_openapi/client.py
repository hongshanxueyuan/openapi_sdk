import logging
import json
import requests
from urllib.parse import urlparse
from . import constants, signature, util


class Client:

    def __init__(self, app_key, app_secret, timeout=constants.REQUEST_TIMEOUT):
        self.app_key = app_key
        self.app_secret = app_secret
        self.timeout = timeout

    def request(self, url, method, params=None, data=None, headers=None, timeout=None):
        method = method.upper()
        assert constants.HTTP_METHOD.is_validate_method(method), 'not validate http method'
        assert '?' not in url, 'query use params, not include in url'
        parsed_url = urlparse(url)
        timeout = timeout or self.timeout
        params = params or {}
        data = data or {}
        headers = headers or {}
        headers = self.build_headers(parsed_url.path, method, headers, params, data)
        logging.debug(
            'openapi request: method: {}\nurl: {}\nheaders: {}\nparams: {}\ndata: {}'.format(
                method, url, headers, params, data
        ))
        resp = requests.request(method, url, params=params, data=data, headers=headers, timeout=timeout)
        return resp

    def build_headers(self, uri, method, headers, params, data):
        _headers = {}
        if 'Date' in headers:
            _headers['Date'] = headers['Date']
        _headers['X-Ca-Timestamp'] = util.DateUtil.get_timestamp()
        _headers['X-Ca-Key'] = self.app_key
        _headers['X-Ca-Nonce'] = util.UUIDUtil.get_uuid()
        _headers['Content-Type'] = headers.get('Content-Type') or constants.CONTENT_TYPE.FORM
        _headers['Accept'] = headers.get('Accept') or constants.CONTENT_TYPE.JSON
        if method == 'POST' and _headers['Content-Type'] != constants.CONTENT_TYPE.FORM:
            _headers['Content-MD5'] = util.MD5Util.get_md5_base64_str(data)
        str_to_sign = signature.build_sign_str(uri, method, _headers, params=params, data=data)
        _headers['X-Ca-Signature-Method'] = 'HmacSHA256'
        _headers['X-Ca-Signature'] = signature.sign(str_to_sign, self.app_secret)
        headers.update(_headers)
        return headers
