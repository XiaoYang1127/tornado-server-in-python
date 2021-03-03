#!/usr/bin/env/python
# _*_coding:utf-8_*_

import httpserver.handler

import logic.test_handler
import logic.test_concurrent
import logic.test_gen
import logic.test_client


HANDLERS = [
    (r"/v1/api/test_handler", logic.test_handler.CTestHandler),
    (r"/v1/api/test_concurrent", logic.test_concurrent.CTestConcurrent),
    (r"/v1/api/test_gen", logic.test_gen.CTestGenHandler),
    (r"/v1/api/test_client", logic.test_client.CTestClientHandler),
    (r"/.*", httpserver.handler.CRequestHandler),
]
