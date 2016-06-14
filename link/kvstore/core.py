# -*- coding: utf-8 -*-

from link.middleware.core import Middleware


class KeyValueStore(Middleware):
    def __init__(self, backend, *args, **kwargs):
        super(KeyValueStore, self).__init__(*args, **kwargs)

        self._backend = backend

    def __getitem__(self, attr):
        return self._backend.get(key=attr)

    def __setitem__(self, attr, val):
        self._backend.put(key=attr, value=val)

    def __delitem__(self, attr):
        self._backend.remove(key=attr)

    def __contains__(self, attr):
        return self._backend.exists(key=attr)

    def __iter__(self):
        return iter(self._backend.keys())
