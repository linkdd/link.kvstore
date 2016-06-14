# -*- coding: utf-8 -*-

from link.middleware.connectable import ConnectableMiddleware


class Driver(ConnectableMiddleware):
    def get(self, key):
        raise NotImplementedError()

    def put(self, key, val):
        raise NotImplementedError()

    def remove(self, key):
        raise NotImplementedError()

    def exists(self, key):
        raise NotImplementedError()

    def keys(self):
        raise NotImplementedError()
