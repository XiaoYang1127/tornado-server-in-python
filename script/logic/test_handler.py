#!/usr/local/env python
# _*_ coding:utf-8 _*_

import httpserver.handler


class CTestHandler(httpserver.handler.CRequestHandler):

    def do_get(self, *args, **kwargs):
        response_data = {
            "status_code": 200,
            "message": "success",
            "payload": self.m_query_params,
        }
        self.response_to_web(response_data)

    def do_post(self, *args, **kwargs):
        response_data = {
            "status_code": 200,
            "message": "success",
            "payload": self.m_query_params,
        }
        self.response_to_web(response_data)

    def do_delete(self, *args, **kwargs):
        response_data = {
            "status_code": 200,
            "message": "success",
            "payload": self.m_query_params,
        }
        self.response_to_web(response_data)

    def do_patch(self, *args, **kwargs):
        response_data = {
            "status_code": 200,
            "message": "success",
            "payload": self.m_query_params,
        }
        self.response_to_web(response_data)

    def do_put(self, *args, **kwargs):
        response_data = {
            "status_code": 200,
            "message": "success",
            "payload": self.m_query_params,
        }
        self.response_to_web(response_data)
