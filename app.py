#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import tornado.ioloop
import tornado.web
import tornado.websocket

from actions.ws import EchoWebSocket
from actions.auth import LoginHandler
from actions.core import MainHandler

settings = {
    'static_path': 'static',
    'template_path': 'template',
    'cookie_secret': 'Upfour',
    'xsrf_cookies': False,
    'debug': True,
    'autoreload': True,
    'login_url': '/login',
}


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/ws', EchoWebSocket),
        (r'/login', LoginHandler),
    ], **settings)

if __name__ == '__main__':
    app = make_app()
    app.listen(8686)
    tornado.ioloop.IOLoop.current().start()


