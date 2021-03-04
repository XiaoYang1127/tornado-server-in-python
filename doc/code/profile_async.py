#!/usr/bin/env/python
# _*_coding:utf-8_*_

import requests

import tornado
import tornado.ioloop
import tornado.web
from concurrent.futures import ThreadPoolExecutor


class Executor(ThreadPoolExecutor):
    """
    创建多线程的线程池，线程池的大小为10
    创建多线程时使用了单例模式，如果Executor的_instance实例已经被创建，则不再创建
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not getattr(cls, '_instance', None):
            cls._instance = ThreadPoolExecutor(max_workers=10)
        return cls._instance


# 全部协程+异步线程池实现，yield在此的作用相当于回调函数
# 经过压力测试发现，此种方式的性能在并发量比较大的情况下，要远远优于纯协程实现方案
class Haha1Handler(tornado.web.RequestHandler):
    # executor在此设计中为设计模式中的享元模式，所有的对象共享executor的值
    executor = Executor()

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        value = self.get_argument("value", default=None)
        result = yield self._process(value)
        self.write(result)

    @tornado.concurrent.run_on_executor  # 增加并发量
    def _process(self, url):
        return 'success'


# 全部协程实现
class Haha2Handler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        value = self.get_argument("value", default=None)
        result = yield tornado.gen.Task(self._process, value)
        self.write(result)

    @tornado.gen.coroutine
    def _process(self, url):
        return 'success'


class WebServerApplication(object):

    def __init__(self, port):
        self.port = port
        self.settings = {'debug': False}

    def make_app(self):
        return tornado.web.Application([
            (r"/gethaha1?", Haha1Handler),
            (r"/gethaha2?", Haha2Handler),
        ], **self.settings)

    def process(self):
        app = self.make_app()
        app.listen(self.port)
        tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    server_port = "10001"
    server = WebServerApplication(server_port)
    server.process()
