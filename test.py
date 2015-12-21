# -*- coding: utf-8 -*-
import base65536


def test_ascii():
    encoded = base65536.encode('hello')
    assert encoded == u'\u9a68\ua36c\u156f'
    assert base65536.decode(encoded) == 'hello'


def test_unicode_decode_error():
    encoded = base65536.encode(u'안녕'.encode('utf-8'))
    assert base65536.decode(encoded).decode('utf-8') == u'안녕'
