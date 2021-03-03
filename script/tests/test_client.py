from tornado.httpclient import HTTPClient, AsyncHTTPClient
from tornado.gen import coroutine


def test1():
    url = 'https://www.baidu.com/'
    http_client = HTTPClient()
    response = http_client.fetch(url)
    print("Body:", response.body)


def test2back(response):
    if response.error:
        print("Error:", response.error)
    else:
        print("Body:", response.body)


http_client = AsyncHTTPClient()
http_client.fetch('https://www.baidu.com/', test2back)
