# -*- coding: utf-8 -*-

from link.middleware.core import Middleware


class KeyValueStore(Middleware):
    """
    Key/Value store middleware providing dict API.

    :param backend: Store driver to use
    :type backend: Driver
    """

    def __init__(self, backend, *args, **kwargs):
        super(KeyValueStore, self).__init__(*args, **kwargs)

        self._backend = backend

    def __getitem__(self, attr):
        return self._backend.get(attr)

    def __setitem__(self, attr, val):
        self._backend.put(attr, val)

    def __delitem__(self, attr):
        self._backend.remove(attr)

    def __contains__(self, attr):
        return self._backend.exists(attr)

    def __iter__(self):
        return iter(self._backend.keys())
