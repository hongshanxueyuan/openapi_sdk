from firacademy_openapi.client import Client

APP_KEY = 'your-app-key'
APP_SECRET = 'your-app-secret'


def get_no_param_request():
    url= 'http://bbafae24be8d4cfeb7524831fd3f2c63-cn-zhangjiakou.alicloudapi.com/openapi/v2/courses/'
    client = Client(APP_KEY, APP_SECRET, timeout=30)
    resp = client.request(url, 'GET')
    return resp


def get_authenticate_and_param_request():
    url= 'http://bbafae24be8d4cfeb7524831fd3f2c63-cn-zhangjiakou.alicloudapi.com/openapi/v1/enrollments/'
    headers = {
        'Authorization': 'Bearer f8rGP14RLbiWAjCki5fVEUCroqF2as',
    }
    params = {
        'offset': '0',
        'limit': '1',
    }
    client = Client(APP_KEY, APP_SECRET, timeout=30)
    resp = client.request(url, 'GET', params=params, headers=headers)
    return resp


def post_data_request():
    url= 'http://bbafae24be8d4cfeb7524831fd3f2c63-cn-zhangjiakou.alicloudapi.com/openapi/v1/auth/login/'
    client = Client(APP_KEY, APP_SECRET, timeout=30)
    data = {
        'password': 'your-password',
        'account': 'your-email@email.com',
    }
    resp = client.request(url, 'POST', data=data)
    return resp
