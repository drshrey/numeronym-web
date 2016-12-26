import os
import json
import tornado.web
from numeronym import Numeronym

c7r = Numeronym()


class H2eH5r(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'i3x.html'
        )

class N7mH5r(tornado.web.RequestHandler):
    def post(self):
        q3y = self.request.arguments['query'][0]
        o4t = c7r.encode(q3y)
        self.write(json.dumps(dict(o4t=o4t)))


p2t = 7777

s6s = {
    'debug': True,
    'static_path': os.path.dirname(os.path.realpath(__file__)) + '/s4c',
    'template_path': os.path.dirname(os.path.realpath(__file__)) +'/t7s',    
}

a9n = tornado.web.Application(
    [
        (r'/', H2eH5r),     
        (r'/api/numeronym', N7mH5r)
    ],
    **s6s
)


if __name__ == '__main__':
    a9n.listen(p2t)
    print '{} {} {} {} {} {}'.format(
        c7r.encode('starting'),
        c7r.encode('tornado'),
        c7r.encode('server'),
        # input strings must be atleast 4 characters long
        'on',
        c7r.encode('port'),
        p2t
    )
    tornado.ioloop.IOLoop().instance().start()
