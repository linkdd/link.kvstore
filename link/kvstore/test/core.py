# -*- coding: utf-8 -*-

from b3j0f.utils.ut import UTCase
from unittest import main
from mock import Mock

from link.kvstore.core import KeyValueStore
from link.kvstore.driver import Driver


class KVStoreTest(UTCase):
    def setUp(self):
        self.backend = Mock()
        self.backend.__class__ = Driver

        self.store = KeyValueStore(self.backend)

    def test_get_item(self):
        attrs = {
            'get.return_value': 'bar'
        }
        self.backend.configure_mock(**attrs)

        result = self.store['foo']

        self.assertEqual(result, 'bar')
        self.backend.get.assert_called_with('foo')

    def test_get_noitem(self):
        attrs = {
            'get.side_effect': KeyError
        }
        self.backend.configure_mock(**attrs)

        with self.assertRaises(KeyError):
            self.store['foo']

        self.backend.get.assert_called_with('foo')

    def test_set_item(self):
        attrs = {
            'put.return_value': None
        }
        self.backend.configure_mock(**attrs)

        self.store['foo'] = 'bar'

        self.backend.put.assert_called_with('foo', 'bar')

    def test_del_item(self):
        attrs = {
            'remove.return_value': None
        }
        self.backend.configure_mock(**attrs)

        del self.store['foo']

        self.backend.remove.assert_called_with('foo')

    def test_del_noitem(self):
        attrs = {
            'remove.side_effect': KeyError
        }
        self.backend.configure_mock(**attrs)

        with self.assertRaises(KeyError):
            del self.store['foo']

        self.backend.remove.assert_called_with('foo')

    def test_contains_item(self):
        attrs = {
            'exists.return_value': True
        }
        self.backend.configure_mock(**attrs)

        result = 'foo' in self.store

        self.assertTrue(result)
        self.backend.exists.assert_called_with('foo')

    def test_iter_keys(self):
        expected = ['foo', 'bar', 'baz']
        attrs = {
            'keys.return_value': expected
        }
        self.backend.configure_mock(**attrs)

        result = [key for key in self.store]

        self.assertEqual(result, expected)
        self.backend.keys.assert_called_with()


if __name__ == '__main__':
    main()
