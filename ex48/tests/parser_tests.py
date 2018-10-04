from nose.tools import *
from ex48 import lexicon
from ex48 import parser

def test_get_subject():
    assert_equal(lexicon.scan("north"), [("direction", "north")])
    result = lexicon.scan("north south east")
    assert_equal(result, [("direction", "north"),
                          ("direction", "south"),
                          ("direction", "east")])
