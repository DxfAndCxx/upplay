#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import tornado.web
from helper.handler import BaseHandler

from helper.poker import Cards
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
        return self.write(json.dumps({'success': True}))


class JiaoZhuHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        """叫主"""
        user = self.current_user
        arg = self.get_argument("zhu")
        return self.write(json.dumps({'success': True, 'data': Cards.diPai}))

