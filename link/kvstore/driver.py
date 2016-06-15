# -*- coding: utf-8 -*-

from link.middleware.connectable import ConnectableMiddleware


class Driver(ConnectableMiddleware):
    """
    Generic driver for accessing Key/Value store.
    """

    def _get(self, conn, key):
        raise NotImplementedError()

    def _put(self, conn, key, val):
        raise NotImplementedError()

    def _remove(self, conn, key):
        raise NotImplementedError()

    def _exists(self, conn, key):
        raise NotImplementedError()

    def _keys(self, conn):
        raise NotImplementedError()

    def get(self, key):
        """
        Get value from the store.

        :param key: Associated key
        :type key: str

        :returns: Value

        :raises KeyError: if key does not exist
        """

        return self._get(self.conn, key)

    def put(self, key, val):
        """
        Set value in the store.

        :param key: Associated key
        :type key: str

        :param val: Value to set
        :type val: any
        """

        self._put(self.conn, key, val)

    def remove(self, key):
        """
        Remove value from the store.

        :param key: Associated key
        :type key: str

        :raises KeyError: if key does not exist
        """

        self._remove(self.conn, key)

    def exists(self, key):
        """
        Check if key exists in store.

        :param key: Key to check for
        :type key: str

        :rtype: bool
        """

        return self._exists(self.conn, key)

    def keys(self):
        """
        Get list of keys in store.

        :returns: List of keys
        :rtype: iterable
        """

        return self._keys(self.conn)
