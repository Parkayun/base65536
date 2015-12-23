.. base65536 documentation master file, created by
   sphinx-quickstart on Wed Dec 23 13:08:07 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

base65536
=========
base65536 Python 2 and 3 implementation.

What is this
~~~~~~~~~~~~
In the `original base65536 project`_ says

   Base64 is used to encode arbitrary binary data as "plain" text using a small, extremely safe repertoire of 64 (well, 65) characters. Base64 remains highly suited to text systems where the range of characters available is very small -- i.e., anything still constrained to plain ASCII. Base64 encodes 6 bits, or 3/4 of an octet, per character.
   However, now that Unicode rules the world, the range of characters which can be considered "safe" in this way is, in many situations, significantly wider. Base65536 applies the same basic principle to a carefully-chosen repertoire of 65,536 (well, 65,792) Unicode code points, encoding 16 bits, or 2 octets, per character.
   In theory, this project could have been a one-liner. In practice, naively taking each pair of bytes and smooshing them together to make a single code point is a bad way to do this because you end up with:

   * Control characters
   * Whitespace
   * Unpaired surrogate pairs
   * Normalization corruption
   * No way to tell whether the final byte in the sequence was there in the original or not


Installation
~~~~~~~~~~~~
.. sourcecode:: bash

   ~ $ python setup.pt install

with pip

.. sourcecode:: bash

   ~ $ pip install base65536


Usage
~~~~~

.. sourcecode:: python

   >>> import base65536
   >>> a = base65536.encode("Hello World")
   >>> print(a)
   驈ꍬ啯ꍲᕤ
   >>> print(base65536.decode(a))
   Hello World

.. _original base65536 project: https://github.com/ferno/base65536

API
~~~

.. toctree::
   :maxdepth: 2

   api/core


License
~~~~~~~
MIT
