from hypothesis import given
from hypothesis.strategies import text
from fncts import *


@given(text(min_size=1))
def test_decode_inverts_encode(s):
    print(s)
    assert decode(encode(s)) == s
