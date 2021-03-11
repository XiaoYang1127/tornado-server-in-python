#!/usr/local/env python
# _*_ coding:utf-8 _*_

import tornado.web
import tornado.gen

import httpserver.handler


class CTestGenHandler(httpserver.handler.CRequestHandler):

    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        self.do_post(*args, callback=self.on_post_back)

    def on_post_back(self, response_data):
        self.response_to_web(response_data)

    @tornado.gen.coroutine
    def do_post(self, *args, **kwargs):
        """
        - test the ``calback`` in tornado.gen.coroutine
        """
        response_data = {
            "status_code": 200,
            "message": "success",
            "payload": self.get_query_params(),
            "in_gen": "test_coroutine_call_back",
        }
        return response_data
