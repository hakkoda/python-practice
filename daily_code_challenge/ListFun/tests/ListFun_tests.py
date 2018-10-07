from nose.tools import *
from ListFun.main import *

def test_find_largest():
    target = [ 1, 2, 3 ]
    largest = find_largest(target)
    assert_equal(3, largest)

def test_find_sum():
    target = [ 1, 2, 3 ]
    target_sum = find_sum(target)
    assert_equal(6, target_sum)

def test_sort_asc():
    target = [ 1, 2, 3 ]
    target_sorted = sort_asc(target)
    assert_equal([ 3, 2, 1 ], target_sorted)

def test_sort_asc():
    target = [ 2, 9, 9, 3, 8, 5, 4, 0, 1 ]
    target_sorted = sort_asc(target)
    assert_equal([ 9, 9, 8, 5, 4, 3, 2, 1, 0 ], target_sorted)
