#!/usr/local/env python
# _*_ coding:utf-8 _*_

import httpserver.handler


class CTestGenHandler(httpserver.handler.CRequestHandler):

    def do_post(self, *args, **kwargs):
        """
        - only test the ``calback`` in tornado.gen.coroutine
        - please see details in ``httpserver.base.post``, ``httpserver.base.on_post``, ``httpserver.base.do_post``
        """
        response_data = {
            "status_code": 200,
            "message": "success",
            "payload": self.get_query_params(),
            "in_gen": "in_gen",
        }
        self.response_to_web(response_data)
        return response_data
