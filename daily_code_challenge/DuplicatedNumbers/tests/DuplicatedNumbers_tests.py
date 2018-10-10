from nose.tools import *
from DuplicatedNumbers.main import DuplicatedNumbers

def test_sort_list():
    dup = DuplicatedNumbers()
    num_list = [ 4, 1, 0, 3, 2 ]
    sorted_list = dup.sort_list(num_list)
    assert_equal(sorted_list, [ 0, 1, 2, 3, 4 ])


def test_has_duplicate():
    dup = DuplicatedNumbers()
    dup_list = [ 1, 1, 2, 3, 4 ]
    has_dups = dup.has_dups(dup_list)
    assert_equal(True, has_dups)

def test_does_not_have_duplicate():
    dup = DuplicatedNumbers()
    dup_list = [ 1, 2, 3, 4 ]
    has_dups = dup.has_dups(dup_list)
    assert_equal(False, has_dups)
