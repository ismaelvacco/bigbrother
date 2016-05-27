import tornado.ioloop
import tornado.web
import os


static_path = "/home/eotica/bigbrother/static"

settings = {
    'debug': True, 
#    'static_path': '/home/eotica/bigbrother/static'
}


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print self.request.arguments
        self.write(self.request.arguments)

def make_app():
    return tornado.web.Application([
        (r'/js/(.*)', tornado.web.StaticFileHandler, {'path': static_path}),
        (r"/", MainHandler),
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
