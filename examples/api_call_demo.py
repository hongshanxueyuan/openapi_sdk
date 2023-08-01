from firacademy_openapi.client import Client

APP_KEY = 'your-app-key'
APP_SECRET = 'your-app-secret'
HOST = 'https://openapi.firacademy.com'


def get_client():
    client = Client(APP_KEY, APP_SECRET, timeout=30)
    return client


def get_no_param_request():
    url= '{}/openapi/v2/courses/'.format(HOST)
    client = get_client()
    resp = client.request(url, 'GET')
    return resp


def get_authenticate_and_param_request():
    url= '{}/openapi/v1/enrollments/'.format(HOST)
    headers = {
        'Authorization': 'Bearer f8rGP14RLbiWAjCki5fVEUCroqF2as',
    }
    params = {
        'offset': '0',
        'limit': '1',
    }
    client = get_client()
    resp = client.request(url, 'GET', params=params, headers=headers)
    return resp


def post_data_request():
    url= '{}/openapi/v1/auth/login/'.format(HOST)
    client = get_client()
    data = {
        'password': 'your-password',
        'account': 'your-email@email.com',
    }
    resp = client.request(url, 'POST', data=data)
    return resp
