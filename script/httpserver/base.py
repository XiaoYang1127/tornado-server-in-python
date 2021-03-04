#!/usr/bin/env/python
# _*_coding:utf-8_*_

import json
import time
import urllib
from functools import partial

import concurrent.futures
import tornado.concurrent
import tornado.gen
import tornado.ioloop
import tornado.web


class CBaseHandler(tornado.web.RequestHandler):
    executor = concurrent.futures.ThreadPoolExecutor(10)

    def __init__(self, application, request, **kwargs):
        tornado.web.RequestHandler.__init__(
            self, application, request, **kwargs)
        self.m_query_params = {}
        self.__timeout = self.ioloop().add_timeout(
            int(time.time()) + 30, partial(self.simple_response, 408))

    def ioloop(self):
        return tornado.ioloop.IOLoop.instance()

    def is_valid_request(self):
        return 1

    def get_query_params(self):
        return self.m_query_params

    def request_summary(self):
        url = urllib.parse.unquote(self.request.uri)
        return "%s %s (%s)" % (self.request.method, url, self.request.remote_ip)

    def headers(self):
        return self.request.headers

    def get_headers(self, key, default=None):
        return self.headers().get(key, default)

    @tornado.web.asynchronous
    def head(self, *args, **kwargs):
        self.do_head(*args, **kwargs)

    def do_head(self, *args, **kwargs):
        self.simple_response(405)

    @tornado.web.asynchronous
    # @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        """
        使用asynchronous decorator，它主要设置_auto_finish为false，
        这样handler的get函数返回的时候tornado就不会关闭与client的连接
        """
        # one
        # self.on_get(*args, **kwargs)

        # two
        self.ioloop().add_callback(self.on_get, *args, **kwargs)

        # three
        # yield tornado.gen.Task(self.on_get, *args, **kwargs)

        # four
        # self.ioloop().call_later(0.001, callback=self.on_get)

    @tornado.gen.coroutine
    @tornado.concurrent.run_on_executor
    def on_get(self, *args, **kwargs):
        self.do_get(*args, **kwargs)

    def do_get(self, *args, **kwargs):
        self.simple_response(405)

    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        self.on_post(*args, callback=self.on_post_back)

    @tornado.gen.coroutine
    def on_post(self, *args, **kwargs):
        return self.do_post(*args, **kwargs)

    def on_post_back(self, *args):
        print(">>>>> %s" % args)

    @tornado.web.asynchronous
    def delete(self, *args, **kwargs):
        self.do_delete(*args, **kwargs)

    def do_delete(self, *args, **kwargs):
        self.simple_response(405)

    @tornado.web.asynchronous
    def patch(self, *args, **kwargs):
        self.do_patch(*args, **kwargs)

    def do_patch(self, *args, **kwargs):
        self.simple_response(405)

    @tornado.web.asynchronous
    def put(self, *args, **kwargs):
        self.do_put(*args, **kwargs)

    def do_put(self, *args, **kwargs):
        self.simple_response(405)

    @tornado.web.asynchronous
    def options(self, *args, **kwargs):
        self.do_options(*args, **kwargs)

    def do_options(self, *args, **kwargs):
        self.simple_response(405)

    def simple_response(self, result, desc=""):
        res_dict = {}
        res_dict["status_code"] = result
        res_dict["message"] = desc
        self.ioloop().add_callback(self._response, res_dict)

    def response_to_web(self, res_dict=None):
        self.ioloop().add_callback(self._response, res_dict)

    def _response(self, chunk=None):
        if self._finished:
            return

        chunk = chunk or {}
        if isinstance(chunk, dict):
            self.set_header("Content-Type", "application/json; charset=utf-8")
            chunk = json.dumps(chunk, ensure_ascii=False)

        self.write(chunk)
        self.finish()

    def on_finish(self):
        self.ioloop().remove_timeout(self.__timeout)
