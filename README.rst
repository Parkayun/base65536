base65536
=========

.. image:: https://secure.travis-ci.org/Parkayun/base65536.svg?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/Parkayun/base65536

.. image:: https://readthedocs.org/projects/base65536/badge/?version=latest
   :target: http://base65536.readthedocs.org/en/latest/
   :alt: :Documentation Status

base65536 Python 2 and 3 implementation.

Installation
------------

.. sourcecode:: bash

   ~ $ python setup.py install

with pip

.. sourcecode:: bash

   ~ $ pip install base65536


Quick start
-----------

.. sourcecode:: python

   >>> import base65536
   >>> a = base65536.encode("Hello World")
   >>> print(a)
   驈ꍬ啯ꍲᕤ
   >>> print(base65536.decode(a))
   Hello World

