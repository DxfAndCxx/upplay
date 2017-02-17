#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
from helper.handler import BaseHandler
from helper.common import room

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        user = self.current_user
        self.render('index.html', user=user)


class ReadyHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        room.member_ready(self.current_user)

