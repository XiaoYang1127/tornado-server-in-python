import tornado.ioloop
import tornado.concurrent

import httpserver.handler


class CTestFutureHandler(httpserver.handler.CRequestHandler):

    def do_get(self, *args, **kwargs):
        """
        use ``Future`` to make a synchronous method asynchronous
        """
        future = tornado.concurrent.Future()

        def callback(a, b):
            for i in range(1000000000):
                pass
            future.set_result(a + b)

        tornado.ioloop.IOLoop.instance().add_callback(callback, 1, 2)

        result = yield future

        response_data = {
            "status_code": 200,
            "message": "success",
            "payload": self.get_query_params(),
            "result": result,
        }
        self.response_to_web(response_data)
