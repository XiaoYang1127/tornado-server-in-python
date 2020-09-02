#!/usr/bin/env/python
# _*_coding:utf-8_*_

import collections

import concurrent.futures
import tornado.concurrent
import tornado.web


# 方案1
class CTestTornado(tornado.web.RequestHandler):
    """
    异步队列的方式
    """

    def __init__(self, application, request, **kwargs):
        tornado.web.RequestHandler.__init__(
            self, application, request, **kwargs)
        self.m_queue = collections.deque()

    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        self.m_queue.append(self.DoGet, *args, **kwargs)

    def DoGet(self, *args, **kwargs):
        pass


# 方案2
class CExecutor(concurrent.futures.ThreadPoolExecutor):
    """
    创建多线程的线程池，线程池的大小为100
    使用单例模式
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not getattr(cls, '_instance', None):
            cls._instance = concurrent.futures.ThreadPoolExecutor(
                max_workers=100)
        return cls._instance


class CTestTornado2(tornado.web.RequestHandler):
    """
    异步 + 100线程池
    """
    # executor为RequestHandler中的一个属性，在使用run_on_executor时，必须要用，不然会报错
    # executor在此设计中为设计模式中的享元模式，所有的对象共享executor的值
    executor = CExecutor()

    def __init__(self, application, request, **kwargs):
        tornado.web.RequestHandler.__init__(
            self, application, request, **kwargs)
        self.m_queue = collections.deque()

    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        self.m_queue.append(self.DoGet, *args, **kwargs)

    @tornado.concurrent.run_on_executor
    def DoGet(self, *args, **kwargs):
        pass


"""
    多实例的测试，这里不再描述，httpserver监听2个端口，由nginx做方向代理，然后进行测试即可
"""
