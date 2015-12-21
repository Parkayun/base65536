# -*- coding: utf-8 -*-
import os
import unicodedata

import pytest

import base65536


SAMPLES_DIRNAME = os.path.join(os.path.dirname(__file__), 'sample-files')
UNICODE_NORMAL_FORMS = ['NFC', 'NFD', 'NFKC', 'NFKD']


@pytest.mark.parametrize('filename', os.listdir(SAMPLES_DIRNAME))
def test_sample_file(filename):
    with open(os.path.join(SAMPLES_DIRNAME, filename)) as f:
        data = f.read()
    encoded = base65536.encode(data)
    for form in UNICODE_NORMAL_FORMS:
        assert unicodedata.normalize(form, encoded) == encoded
    assert base65536.decode(encoded) == data


def test_ascii():
    encoded = base65536.encode('hello')
    assert encoded == u'\u9a68\ua36c\u156f'
    assert base65536.decode(encoded) == 'hello'


def test_non_ascii():
    encoded = base65536.encode(u'안녕'.encode('utf-8'))
    assert base65536.decode(encoded).decode('utf-8') == u'안녕'
