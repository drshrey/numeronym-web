import os
import json
import tornado.web
from numeronym import Numeronym

c7r = Numeronym()


class H2eH5r(tornado.web.RequestHandler):
    def get(self):
        print "Returning index page!"
        self.render(
            'i3x.html'
        )

class N7mH5r(tornado.web.RequestHandler):
    def post(self):
        if self.request.arguments['q3y'] is not None and len(self.request.arguments) > 0:
            q3y = self.request.arguments['q3y'][0]
            # handle integer
            try:
                int(q3y)
                return self.write(json.dumps(dict(o4t="no #s or symbols")))                
            except ValueError:
                pass

            print "Numeronyming query: {}".format(q3y)
            s3t = q3y.split(' ')
            o4t = ''
            for word in s3t:
                try:
                    o4t += c7r.encode(word) + ' '
                except Exception:
                    o4t += word + ' '

            print "O4t: {}".format(o4t)
            self.write(json.dumps(dict(o4t=o4t)))
        else:
            self.write()


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
