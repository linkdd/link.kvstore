# -*- coding: utf-8 -*-

from link.middleware.core import Middleware, register_middleware
from link.kvstore.driver import Driver


@register_middleware
class KeyValueStore(Middleware):
    """
    Key/Value store middleware providing dict API.

    :param backend: Store driver to use
    :type backend: Driver
    """

    __constraints__ = [Driver]
    __protocols__ = ['kvstore']

    def __getitem__(self, attr):
        if isinstance(attr, tuple):
            return self.get_child_middleware().multiget(attr)

        else:
            return self.get_child_middleware().get(attr)

    def __setitem__(self, attr, val):
        if isinstance(attr, tuple):
            self.get_child_middleware().multiput(attr, val)

        else:
            self.get_child_middleware().put(attr, val)

    def __delitem__(self, attr):
        if isinstance(attr, tuple):
            self.get_child_middleware().multiremove(attr)

        else:
            self.get_child_middleware().remove(attr)

    def __contains__(self, attr):
        if isinstance(attr, tuple):
            return all(self.get_child_middleware().multiexists(attr))

        else:
            return self.get_child_middleware().exists(attr)

    def __iter__(self):
        return iter(self.get_child_middleware().keys())

    def disconnect(self):
        self.get_child_middleware().disconnect()

    def __del__(self):
        self.disconnect()
