# tests.py
from fncts import *


def test_1():
    s = "a"
    assert decode(encode(s)) == "a"


def test_2():
    s = "abcd"
    assert decode(encode(s)) == "abcd"
