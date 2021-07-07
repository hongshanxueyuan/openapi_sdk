import base64
import hashlib
import hmac


def build_sign_str(uri, method, headers, params=None, data=None):
    lf = '\n'
    string_to_sign = []
    string_to_sign.append(method)

    need_signed_headers = ['Accept', 'Content-MD5', 'Content-Type', 'Date']
    for _header in need_signed_headers:
        string_to_sign.append(lf)
        _value = headers.get(_header)
        if _value:
            string_to_sign.append(_value)

    string_to_sign.append(lf)
    string_to_sign.append(_format_header(headers))
    string_to_sign.append(_build_resource(uri, params, data))

    return ''.join(string_to_sign)


def _build_resource(uri, params, data):
    params = params or {}
    data = data or {}
    body = {}
    if params:
        body.update(params)
    if data:
        body.update(data)
    resource = []
    resource.append(uri)
    if body:
        resource.append('?')
        param_list = sorted(body.keys())
        first = True
        for key in param_list:
            if not first:
                resource.append('&')
            first = False

            if body[key]:
                resource.append(key)
                resource.append('=')
                resource.append(body[key])
            else:
                resource.append(key)
    if resource is None:
        return ''
    return ''.join(str(x) for x in resource)


def _format_header(headers):
    headers = headers or {}
    lf = '\n'
    temp_headers = []
    if len(headers) > 0:
        header_list = sorted(headers.keys())
        signature_headers = []
        for k in header_list:
            if k.startswith('X-Ca-'):
                temp_headers.append(k)
                temp_headers.append(':')
                temp_headers.append(str(headers[k]))
                temp_headers.append(lf)
                signature_headers.append(k)
        headers['X-Ca-Signature-Headers'] = ','.join(signature_headers)
    return ''.join(temp_headers)


def sign(source, secret):
    key = bytes(secret, encoding='utf-8')
    h = hmac.new(key, source.encode('utf-8'), hashlib.sha256)
    signature = base64.encodestring(h.digest()).strip()
    return signature
