import tornado.concurrent
import tornado.gen
import tornado.ioloop

import httpserver.handler


class CTestFutureHandler(httpserver.handler.CRequestHandler):

    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        self.ioloop().add_callback(self.do_get, *args, **kwargs)

    @tornado.gen.coroutine
    @tornado.concurrent.run_on_executor
    def do_get(self, *args, **kwargs):
        """
        use ``Future`` to make a synchronous method asynchronous
        but, still blocking the other requests except using ``run_on_executor``
        """
        future = tornado.concurrent.Future()

        def logic_func(a, b):
            for i in range(1000000000):
                pass
            future.set_result(a + b)

        tornado.ioloop.IOLoop.instance().add_callback(logic_func, 1, 2)

        result = yield future

        response_data = {
            "status_code": 200,
            "message": "success",
            "payload": self.get_query_params(),
            "result": result,
            "test_concurrent2":"test_concurrent2",
        }
        self.response_to_web(response_data)
