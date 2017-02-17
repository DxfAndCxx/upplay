#!/usr/bin/env python
# -*- coding: utf-8 -*-


from helper.common import permitUser
import tornado.web
import tornado.websocket


def get_current_user(handler):
    user = handler.get_secure_cookie("user")
    user = user.decode('utf-8')
    if user not in permitUser:
        handler.set_status(401)
        raise tornado.web.Finish('你没有权限访问此页面')
    return user


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return get_current_user(self)


class BaseWebSocketHandler(tornado.websocket.WebSocketHandler):
    def get_current_user(self):
        return get_current_user(self)




