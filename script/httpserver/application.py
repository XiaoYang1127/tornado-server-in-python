#!/usr/bin/env/python
# _*_coding:utf-8_*_

import httpserver.handler

import logic.test_handler
import logic.test_coroutine_call_back
import logic.test_async_http_client
import logic.test_concurrent
import logic.test_concurrent2


HANDLERS = [
    (r"/v1/api/test_handler", logic.test_handler.CTestHandler),
    (r"/v1/api/test_coroutine_call_back", logic.test_coroutine_call_back.CTestGenHandler),
    (r"/v1/api/test_async_http_client", logic.test_async_http_client.CTestClientHandler),
    (r"/v1/api/test_concurrent", logic.test_concurrent.CTestConcurrent),
    (r"/v1/api/test_concurrent2", logic.test_concurrent2.CTestFutureHandler),
    (r"/.*", httpserver.handler.CRequestHandler),
]
