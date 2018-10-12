from nose.tools import *
from RangeCheck.main import RangeCheck

def test_run():
    range_check = RangeCheck()

    #            0  1  2  3  4  5  6
    num_list = [ 6, 2, 3, 4, 0, 7, 8 ]

    first = 0
    last = 1
    index = range_check.run(first, last, num_list)
    assert_equal(index, 0)

    first = 0
    last = 2
    index = range_check.run(first, last, num_list)
    assert_equal(index, 1)

    first = 0
    last = 3
    index = range_check.run(first, last, num_list)
    assert_equal(index, 1)

    first = 0
    last = 4
    index = range_check.run(first, last, num_list)
    assert_equal(index, 1)

    first = 0
    last = 5
    index = range_check.run(first, last, num_list)
    assert_equal(index, 4)

def test_sort_asc():
    range_check = RangeCheck()
    num_list = [ 6, 2, 3, 4, 0, 7, 8 ]
    sorted_list = range_check.sort_asc(num_list)
    assert_equal(sorted_list, [ 0, 2, 3, 4, 6, 7, 8 ])
