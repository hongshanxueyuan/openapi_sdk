OpenAPI SDK for firacademy
===

Usage
---

    clone(unzip code)
    pip install -r requirements.txt
    pip install -e .


API Call Examples
---

    from firacademy_openapi.client import Client

    APP_KEY = 'your-app-key'
    APP_SECRET = 'your-app-secret'


    url= 'http://bbafae24be8d4cfeb7524831fd3f2c63-cn-zhangjiakou.alicloudapi.com/openapi/v2/courses/'
    client = Client(APP_KEY, APP_SECRET, timeout=30)
    resp = client.request(url, 'GET')
    print(resp.content)
    print(resp.json())

more example see `examples/api_call_demo.py`
