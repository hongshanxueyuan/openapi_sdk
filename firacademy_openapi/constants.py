REQUEST_TIMEOUT = 60 * 3

class SYSTEM_HEADERS:
    X_CA_SIGNATURE = 'X-Ca-Signature'
    X_CA_SIGNATURE_HEADERS = 'X-Ca-Signature-Headers'
    X_CA_TIMESTAMP = 'X-Ca-Timestamp'
    X_CA_NONCE = 'X-Ca-Nonce'
    X_CA_KEY = 'X-Ca-Key'


class HTTP_HEADERS:
    ACCEPT = 'Accept'
    CONTENT_MD5 = 'Content-MD5'
    CONTENT_TYPE = 'Content-Type'
    USER_AGENT = 'User-Agent'
    DATE = 'Date'


class HTTP_PROTOCOL:
    HTTP = 'http'
    HTTPS = 'https'


class HTTP_METHOD:
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'
    HEADER = 'HEADER'
    OPTIONS = 'OPTIONS'

    @classmethod
    def is_validate_method(cls, method):
        return method in (
            cls.GET, cls.POST, cls.PUT, cls.PATCH, cls.DELETE, cls.OPTIONS, cls.HEADER
        )


class CONTENT_TYPE:
    FORM = 'application/x-www-form-urlencoded'
    STREAM = 'application/octet-stream'
    JSON = 'application/json'
    XML = 'application/xml'
    TEXT = 'application/text'


class BODY_TYPE:
    FORM = 'FORM'
    STREAM = 'STREAM'
