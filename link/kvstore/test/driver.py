# -*- coding: utf-8 -*-

from b3j0f.utils.ut import UTCase
from mock import MagicMock
from unittest import main

from link.kvstore.driver import Driver


class DriverTest(UTCase):
    def setUp(self):
        self.conn = 'myconn'

        self.driver = Driver()
        self.driver._connect = MagicMock(return_value=self.conn)
        self.driver._disconnect = MagicMock()
        self.driver._isconnected = MagicMock(
            side_effect=lambda conn: conn is not None
        )

    def tearDown(self):
        self.driver.disconnect()

        self.driver._connect.assert_called_once_with()
        self.driver._disconnect.assert_called_once_with(self.conn)
        self.driver._isconnected.assert_any_call(self.conn)

    def test_get_item(self):
        self.driver._get = MagicMock(return_value='bar')

        result = self.driver.get('foo')

        self.assertEqual(result, 'bar')
        self.driver._get.assert_called_with(self.conn, 'foo')

    def test_get_noitem(self):
        self.driver._get = MagicMock(side_effect=KeyError)

        with self.assertRaises(KeyError):
            self.driver.get('foo')

        self.driver._get.assert_called_with(self.conn, 'foo')

    def test_get_multiitem(self):
        expected = ['bar', 'baz']
        self.driver._multiget = MagicMock(return_value=expected)

        result = self.driver.multiget(('foo', 'bar'))

        self.assertEqual(result, expected)
        self.driver._multiget.assert_called_with(self.conn, ('foo', 'bar'))

    def test_put_item(self):
        self.driver._put = MagicMock()

        self.driver.put('foo', 'bar')

        self.driver._put.assert_called_with(self.conn, 'foo', 'bar')

    def test_put_multiitem(self):
        self.driver._multiput = MagicMock()

        self.driver.multiput(('foo', 'bar'), ['bar', 'baz'])

        self.driver._multiput.assert_called_with(
            self.conn,
            ('foo', 'bar'),
            ['bar', 'baz']
        )

    def test_del_item(self):
        self.driver._remove = MagicMock()

        self.driver.remove('foo')

        self.driver._remove.assert_called_with(self.conn, 'foo')

    def test_del_multiitem(self):
        self.driver._multiremove = MagicMock()

        self.driver.multiremove(('foo', 'bar'))

        self.driver._multiremove.assert_called_with(self.conn, ('foo', 'bar'))

    def test_contains_item(self):
        self.driver._exists = MagicMock(return_value=True)

        result = self.driver.exists('foo')

        self.assertTrue(result)
        self.driver._exists.assert_called_with(self.conn, 'foo')

    def test_contains_multiitem(self):
        expected = [True, False]
        self.driver._multiexists = MagicMock(return_value=expected)

        result = self.driver.multiexists(('foo', 'bar'))

        self.assertEqual(result, expected)
        self.driver._multiexists.assert_called_with(self.conn, ('foo', 'bar'))

    def test_get_keys(self):
        expected = ['foo', 'bar', 'baz']
        self.driver._keys = MagicMock(return_value=expected)

        result = self.driver.keys()

        self.assertEqual(result, expected)
        self.driver._keys.assert_called_with(self.conn)


if __name__ == '__main__':
    main()
