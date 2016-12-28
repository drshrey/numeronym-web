import os
import json
import tornado.web
import tornado.ioloop
from tornado.web import authenticated
from tornado import gen
import dataset
from tools import crypto
from numeronym import Numeronym

c7r = Numeronym()

mypath = os.path.dirname(os.path.realpath(__file__))
DATASTORE_PATH = 'sqlite:///%s/datastore.db' % mypath
datastore = dataset.connect(DATASTORE_PATH)

# create cookie_secret if it doesn't exist
if not os.path.exists(mypath + '/cookie_secret'):
    with open(mypath + '/cookie_secret', 'wb') as outfile:
        outfile.write(bytes(crypto.random_integer(10**4)))

with open(mypath + '/cookie_secret', 'rb') as infile:
    COOKIE_SECRET = infile.read()


class BaseHandler(tornado.web.RequestHandler):
    # you can edit this class to change all other RequestHandlers
    pass


class AuthenticatedHandler(BaseHandler):
    def get_current_user(self):
        return self.get_secure_cookie(
            'user',
            max_age_days=10
        )



class LogoutHandler(AuthenticatedHandler):
    def get(self):
        self.set_secure_cookie('user', '')
        self.redirect('/')


class LoginHandler(AuthenticatedHandler):

    @gen.coroutine
    def post(self):
        user = self.get_body_argument('user')
        password = self.get_body_argument('password')
        user_entry = datastore['users'].find_one(user=user)

        # valid login
        if user_entry is not None and crypto.hash(
            password,
            user,
            user_entry['salt']
        ) == user_entry['hash']:

            self.set_secure_cookie(
                'user',
                user,
                expires_days=3
            )
            self.redirect('/')

        # invalid login
        else:
            yield gen.sleep(1)
            self.write('Bad Login Info')



class SignupHandler(AuthenticatedHandler):

    @gen.coroutine
    def post(self):
        yield gen.sleep(0.5)
        user = self.get_body_argument('user')
        if datastore['users'].find_one(user=user) is not None:
            self.write('Bad Signup')

        else:
            password = self.get_body_argument('password')
            salt = crypto.salt()
            user_id = crypto.user_id()
            datastore['users'].insert({
                'user_id': user_id,
                'user': user,
                'salt': salt,
                'hash': crypto.hash(password, user, salt),
            })
            self.set_secure_cookie(
                'user',
                user,
                expires_days=3
            )


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

            print "Numeronym-ing query: {}".format(q3y)
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
