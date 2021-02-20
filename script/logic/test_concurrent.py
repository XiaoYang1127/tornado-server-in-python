#!/usr/local/env python
# _*_ coding:utf-8 _*_

import time
from tornado import httpclient

import httpserver.handler


class CTestConcurrent(httpserver.handler.CRequestHandler):

    # def do_get(self, *args, **kwargs):
    #     """
    #     use `time.sleep` to test tornado concurrent and asynchronous
    #     """
    #     time.sleep(10)
    #     response_data = {
    #         "status_code": 200,
    #         "message": "success",
    #         "payload": self.get_query_params(),
    #     }
    #     self.response_to_web(response_data)

    def do_get(self, *args, **kwargs):
        """
        test tornado.web.asynchronous

        - 使用AsyncHttpClient，fetch的时候提供callback函数，
        这样当fetch http请求完成的时候才会去调用on_response，而不会阻塞。
        - on_response调用完成之后通过finish结束与client的连接
        """
        http = httpclient.AsyncHTTPClient()
        http.fetch("http://friendfeed.com/", self.on_response)

    def on_response(self, response):
        response_data = {
            "status_code": 200,
            "message": "success",
            "payload": self.get_query_params(),
        }
        self.response_to_web(response_data)
