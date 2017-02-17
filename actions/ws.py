#!/usr/bin/env python
# -*- coding: utf-8 -*-
from helper.handler import BaseWebSocketHandler
from helper.common import room

class EchoWebSocket(BaseWebSocketHandler):
    def open(self):
        room.enter(self)
        current_user = self.current_user
        print 'WebSocket opened'


    def on_message(self, message):
        """"""
        user = self.current_user
        room.broadcast(user + u' comming')


    def on_close(self):
        room.leave(self)
        print 'WebSocket closed'


