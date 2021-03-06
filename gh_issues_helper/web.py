
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


def serve(config):
    app = make_app()
    app.listen(config.PORT)
    tornado.ioloop.IOLoop.current().start()
