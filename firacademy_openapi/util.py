import base64
import hashlib
import sys
import time
import uuid

from urllib.parse import quote


class DateUtil:
    TIME_ZONE = "GMT"
    FORMAT_ISO_8601 = "%Y-%m-%dT%H:%M:%SZ"
    FORMAT_RFC_2616 = "%a, %d %b %Y %X GMT"

    @classmethod
    def get_iso_8061_date(cls):
        return time.strftime(cls.FORMAT_ISO_8601, time.gmtime())

    @classmethod
    def get_rfc_2616_date(cls):
        return time.strftime(cls.FORMAT_RFC_2616, time.gmtime())

    @classmethod
    def get_timestamp(cls):
        return str(int(time.time() * 1000))


class ParamUtil:

    @classmethod
    def percent_encode(cls, encode_str):
        encode_str = str(encode_str)
        if sys.stdin.encoding is None:
            res = quote(encode_str.decode('cp936').encode('utf8'), '')
        else:
            res = quote(encode_str.decode(sys.stdin.encoding).encode('utf8'), '')
        res = res.replace('+', '%20')
        res = res.replace('*', '%2A')
        res = res.replace('%7E', '~')
        return res


class UUIDUtil:

    @classmethod
    def get_uuid(cls):
        return str(uuid.uuid4())


class MD5Util:

    @classmethod
    def get_md5(cls, content, encoding='utf-8'):
        m = hashlib.md5(content.encode(encoding)).hexdigest()
        return m.digest()

    @classmethod
    def get_md5_base64_str(cls, content):
        return base64.encodestring(cls.get_md5(content)).strip()
