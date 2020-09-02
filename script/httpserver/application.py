#!/usr/bin/env/python
# _*_coding:utf-8_*_

import logic.test_handler
import httpserver.handler


HANDLERS = [
    (r"/v1/api/test_handler", logic.test_handler.CTestHandler),
    (r"/.*", httpserver.handler.CRequestHandler),
]
