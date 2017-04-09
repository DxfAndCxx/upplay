#!/usr/bin/env python
# -*- coding: utf-8 -*-
from poker import Cards

permitUser = [u'土土土', u'超超', u'雪峰', u'小雪']


class Store(object):
    def __init__(self):
        self.path = ''

    def load(self):
        pass



class Member(object):
    user = None
    connects = []
    ready = None

    def __init__(self, handler):
        self.user = handler.current_user
        self.connects.append(handler)


    def add_connect(self, handler):
        self.connects.append(handler)


    def remove_connect(self, handler):
        self.connects.remove(handler)



class Room(object):
    _members =  {}
    status = None
    _memberslist = []

    def __init__(self):
        pass


    def get_member_by_user(self, user):
        return self._members[user]


    def new_member_come(self, handler):
        user = handler.current_user
        member = Member(handler)
        self._members[user] = member
        self._memberslist.append(user)

        # TODO: 发送广播：xxx 进入房间

    def member_leave(self, handler):
        """房间里成员离开"""
        user = handler.current_user
        self._members.pop(user)

        # TODO: 发送广播：xxx 离开房间

    def enter(self, handler):
        user = handler.current_user
        if user not in self._members:  # 新成员进入房间
            self.new_member_come(handler)
        else:              # 房间成员打开另一个页面
            member = self._members[user]
            member.add_connect(handler)


    def leave(self, handler):
        user = handler.current_user
        if user in self._members:
            member = self._members[user]
            if handler in member.connects:
                member.remove_connect(handler)

            if len(member.connects) <= 0:    # 成员离开房间
                self.member_leave(handler)


    def broadcast(self, data):
        for user, member in self._members.items():
            for handler in member.connects:
                handler.write_message(data)

    def broadcast_to_user(self, user, data):
        handlers = self._members[user]
        for handler in handlers:
            handler.write_message(data)


    def member_ready(self, user):
        member = self._members[user]
        member.ready = True

        all_ready = True
        for u, mem in self._members.items():
            if mem.ready:
                # TODO: 发送广播：xxx 已准备
                pass
            else:
                all_ready = False

        if all_ready:
            cards = Cards.deal_card()
            for i, user in enumerate(self._members.keys()):
                self.broadcast_to_user(user, cards[i])
            # TODO: 所有人都准备好，广播发牌

room = Room()

