#!/usr/bin/env/python
# _*_coding:utf-8_*_

import os
import functools
import datetime

import tornado
import tornado.gen
import tornado.ioloop
import tornado.web
from concurrent.futures import ThreadPoolExecutor


# 同步1
class SyncHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        # 耗时的代码
        os.system("ping -c 2 www.google.com")
        self.finish('It works')


# 异步1
# 通过tornado的IO循环，把可以把耗时的任务放到后台异步计算，请求可以接着做别的计算
class AsyncHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        tornado.ioloop.IOLoop.instance().add_timeout(
            1, callback=functools.partial(self.ping, 'www.google.com'))
        # do something others
        self.finish('It works')

    @tornado.gen.coroutine
    def ping(self, url):
        os.system("ping -c 2 {}".format(url))
        return 'after'


# 异步2
# 经常有一些耗时的任务完成之后，我们需要其计算的结果
# 在并发量很小的情况下，IO本身拉开的差距并不大。甚至协程和同步性能差不多
# yield挂起函数协程，尽管没有block主线程，因为需要处理返回值，挂起到响应执行还是有时间等待
class AsyncTaskHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        # yield 结果
        response = yield tornado.gen.Task(self.ping, ' www.google.com')
        print('response', response)
        self.finish('hello')

    @tornado.gen.coroutine
    def ping(self, url):
        os.system("ping -c 2 {}".format(url))
        return 'after'


# 异步3
# 线程池
class FutureHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(10)

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        url = 'www.google.com'
        tornado.ioloop.IOLoop.instance().add_callback(functools.partial(self.ping, url))
        self.finish('It works')

    @tornado.concurrent.run_on_executor
    def ping(self, url):
        os.system("ping -c 2 {}".format(url))


# 异步4
# 线程池
class Executor(ThreadPoolExecutor):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not getattr(cls, '_instance', None):
            cls._instance = ThreadPoolExecutor(max_workers=10)
        return cls._instance


class FutureResponseHandler(tornado.web.RequestHandler):
    executor = Executor()

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        future = Executor().submit(self.ping, 'www.google.com')

        response = yield tornado.gen.with_timeout(datetime.timedelta(10), future, quiet_exceptions=tornado.gen.TimeoutError)

        if response:
            print('response', response.result())

    @tornado.concurrent.run_on_executor
    def ping(self, url):
        os.system("ping -c 1 {}".format(url))
        return 'after'
