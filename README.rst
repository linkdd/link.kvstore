link.kvstore
============

**link.kvstore** is a database agnostic key/value store API.

See documentation_ for more informations.

.. _documentation: https://linkkvstore.readthedocs.io

.. image:: https://img.shields.io/pypi/l/link.kvstore.svg?style=flat-square
   :target: https://pypi.python.org/pypi/link.kvstore/
   :alt: License

.. image:: https://img.shields.io/pypi/status/link.kvstore.svg?style=flat-square
   :target: https://pypi.python.org/pypi/link.kvstore/
   :alt: Development Status

.. image:: https://img.shields.io/pypi/v/link.kvstore.svg?style=flat-square
   :target: https://pypi.python.org/pypi/link.kvstore/
   :alt: Latest release

.. image:: https://img.shields.io/pypi/pyversions/link.kvstore.svg?style=flat-square
   :target: https://pypi.python.org/pypi/link.kvstore/
   :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/implementation/link.kvstore.svg?style=flat-square
   :target: https://pypi.python.org/pypi/link.kvstore/
   :alt: Supported Python implementations

.. image:: https://img.shields.io/pypi/wheel/link.kvstore.svg?style=flat-square
   :target: https://travis-ci.org/linkdd/link.kvstore
   :alt: Download format

.. image:: https://travis-ci.org/linkdd/link.kvstore.svg?branch=master&style=flat-square
   :target: https://travis-ci.org/linkdd/link.kvstore
   :alt: Build status

.. image:: https://coveralls.io/repos/github/linkdd/link.kvstore/badge.svg?style=flat-square
   :target: https://coveralls.io/r/linkdd/link.kvstore
   :alt: Code test coverage

.. image:: https://img.shields.io/pypi/dm/link.kvstore.svg?style=flat-square
   :target: https://pypi.python.org/pypi/link.kvstore/
   :alt: Downloads

.. image:: https://landscape.io/github/linkdd/link.kvstore/master/landscape.svg?style=flat-square
   :target: https://landscape.io/github/linkdd/link.kvstore/master
   :alt: Code Health

.. image:: https://www.quantifiedcode.com/api/v1/project/1285968364df4253a82e3b1543c185e3/badge.svg
  :target: https://www.quantifiedcode.com/app/project/1285968364df4253a82e3b1543c185e3
  :alt: Code issues

Installation
------------

.. code-block:: text

   pip install link.kvstore

Features
--------

 * database agnostic
 * dict API to access key/value store

Examples
--------

Getting a backend:

.. code-block:: python

   from link.middleware.core import Middleware

   # Instanciate a K/V store with Riak backend
   store = Middleware.get_middleware_by_uri(
       'kvstore+riak://localhost:8087/mybuckettype/mybucket?protocol=pbc'
   )
   # Instanciate a K/V store with SQL backend
   store = Middleware.get_middleware_by_uri(
       'kvstore+sql://localhost:5432/database/table'
   )

Accessing data:

.. code-block:: python

   store['foo'] = 'bar'
   assert store['foo'] == 'bar'
   assert 'foo' in store

   for key in store:
       print(key)

   del store['foo']
