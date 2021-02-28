#!/usr/local/env python
# _*_ coding:utf-8 _*_

import httpserver.handler


class CTestConcurrent(httpserver.handler.CRequestHandler):

    # def do_get(self, *args, **kwargs):
    #     import threading
    #     threading.Thread(target=self.do_get1).start()

    # def do_get1(self):
    #     for i in range(1000000000):
    #         pass

    #     response_data = {
    #         "status_code": 200,
    #         "message": "success",
    #         "payload": self.get_query_params(),
    #         "in_concurrent": "in_concurrent",
    #     }
    #     self.response_to_web(response_data)

    # def do_get(self, *args, **kwargs):
    #     """
    #     test tornado.web.asynchronous

    #     - 使用AsyncHttpClient，fetch的时候提供callback函数，
    #     这样当fetch http请求完成的时候才会去调用on_response，而不会阻塞。
    #     - on_response调用完成之后通过finish结束与client的连接
    #     """
    #
    #     from tornado import httpclient
    #     http = httpclient.AsyncHTTPClient()
    #     http.fetch("http://friendfeed.com/", callback=self.on_response)

    # def on_response(self, response):
    #     response_data = {
    #         "status_code": 200,
    #         "message": "success",
    #         "payload": self.get_query_params(),
    #         "in_concurrent": "in_concurrent",
    #
    #     }
    #     self.response_to_web(response_data)

    def do_get(self, *args, **kwargs):
        for i in range(1000000000):
            pass

        response_data = {
            "status_code": 200,
            "message": "success",
            "payload": self.get_query_params(),
            "in_concurrent": "in_concurrent",
        }
        self.response_to_web(response_data)
