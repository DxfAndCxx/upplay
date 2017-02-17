#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from helper.common import permitUser
from helper.handler import BaseHandler

class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        name = self.get_argument("name")
        if name not in permitUser:
            self.set_status(403)
            raise tornado.web.Finish('你没有权限访问此页面')

        self.set_secure_cookie("user", self.get_argument("name"))
        self.redirect('/')

