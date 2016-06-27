# -*- coding: utf-8 -*-

from link.middleware.connectable import ConnectableMiddleware


class Driver(ConnectableMiddleware):
    """
    Generic driver for accessing Key/Value store.
    """

    def _get(self, conn, key):
        raise NotImplementedError()

    def _multiget(self, conn, keys):
        return [
            self._get(conn, key)
            for key in keys
        ]

    def _put(self, conn, key, val):
        raise NotImplementedError()

    def _multiput(self, conn, keys, vals):
        for k, v in zip(keys, vals):
            self._put(conn, k, v)

    def _remove(self, conn, key):
        raise NotImplementedError()

    def _multiremove(self, conn, keys):
        for key in keys:
            self._remove(conn, key)

    def _exists(self, conn, key):
        raise NotImplementedError()

    def _multiexists(self, conn, keys):
        return [
            self._exists(conn, key)
            for key in keys
        ]

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

    def multiget(self, keys):
        """
        Get values from the store.

        :param keys: Associated keys
        :type keys: list

        :returns: Values

        :raises KeyError: if one key does not exist
        """

        return self._multiget(self.conn, keys)

    def put(self, key, val):
        """
        Set value in the store.

        :param key: Associated key
        :type key: str

        :param val: Value to set
        :type val: any
        """

        self._put(self.conn, key, val)

    def multiput(self, keys, vals):
        """
        Set values in the store.

        :param keys: Associated keys
        :type keys: list

        :param vals: Values to set
        :type val: any
        """

        self._multiput(self.conn, keys, vals)

    def remove(self, key):
        """
        Remove value from the store.

        :param key: Associated key
        :type key: str

        :raises KeyError: if key does not exist
        """

        self._remove(self.conn, key)

    def multiremove(self, keys):
        """
        Remove values from the store.

        :param keys: Associated keys
        :type keys: list

        :raises KeyError: if one key does not exist
        """

        self._multiremove(self.conn, keys)

    def exists(self, key):
        """
        Check if key exists in store.

        :param key: Key to check for
        :type key: str

        :rtype: bool
        """

        return self._exists(self.conn, key)

    def multiexists(self, keys):
        """
        Check if keys exists in store.

        :param keys: Keys to check for
        :type keys: list

        :rtype: list
        """

        return self._multiexists(self.conn, keys)

    def keys(self):
        """
        Get list of keys in store.

        :returns: List of keys
        :rtype: iterable
        """

        return self._keys(self.conn)
