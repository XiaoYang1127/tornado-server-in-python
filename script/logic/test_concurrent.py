#!/usr/local/env python
# _*_ coding:utf-8 _*_

import httpserver.handler


class CTestConcurrent(httpserver.handler.CRequestHandler):

    def do_get(self, *args, **kwargs):
        """
        test blocking code in `concurrent.futures.ThreadPoolExecutor`
        """
        for i in range(1000000000):
            pass

        response_data = {
            "status_code": 200,
            "message": "success",
            "payload": self.get_query_params(),
            "in_concurrent": "in_concurrent",
        }
        self.response_to_web(response_data)
