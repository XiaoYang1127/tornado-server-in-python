#!/usr/bin/env/python
# _*_coding:utf-8_*_

import httpserver.http_client as http_client


URL = "http://localhost:8080"


def do_test_http():
    test_post()
    test_get()


def test_post():
    """
    测试POST请求
    """

    url = "%s/v1/api/test_handler" % URL
    headers = {
        "content-type": "application/json",
        "secret_key": "secret_key",
    }
    post_data = {
        "x": 1,
        "b": "A",
        "hello": "中国"
    }
    http_client.http_request("post", url, headers=headers, json=post_data, callback=test_http_back)


def test_get():
    """
    测试GET请求
    """

    url = "%s/v1/api/test_handler?x=1&b=A" % URL
    headers = {
        "content-type": "application/json",
        "secret_key": "secret_key",
    }
    http_client.http_request("get", url, headers=headers, callback=test_http_back)


def test_http_back(result, data):
    print("test_http_back result:%s data:%s" % (result, data))
