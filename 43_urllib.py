#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
import json


# with request.urlopen('https://api.github.com/') as f:
#     print(f.status, f.reason)
#     for k, v in f.getheaders():
#         print(k, ':', v)
# req = request.Request('https://api.github.com/')
# req.add_header('User-Agent',
#                'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print(f.status, f.reason)
#     for k, v in f.getheaders():
#         print(k, ':', v)
#     print(f.read().decode('utf-8'))


def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read().decode('utf-8')
        return json.loads(data)
        print(js)


# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')
