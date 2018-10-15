from nose.tools import *
from LinkedList.main import LinkedList
from LinkedList.main import Node

def test_add_1():
    linked_list = LinkedList()
    linked_list.add(1)
    assert_equal(linked_list.top.data, 1)
    assert_equal(linked_list.get_last().data, 1)

def test_add_2():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    assert_equal(linked_list.top.data, 1)
    assert_equal(linked_list.get_last().data, 2)

def test_size_0():
    linked_list = LinkedList()
    assert_equal(linked_list.size(), 0)

def test_size_1():
    linked_list = LinkedList()
    linked_list.add(1)
    assert_equal(linked_list.size(), 1)

def test_size_2():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    assert_equal(linked_list.size(), 2)

def test_to_array():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    list_array = linked_list.to_array()
    assert_equal([1,2], list_array)

def test_insert():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(4)
    linked_list.insert(2, 3)    # insert value 3 into index 2
    list_array = linked_list.to_array()
    assert_equal([1,2,3,4], list_array)

def test_insert_1():
    linked_list = LinkedList()
    linked_list.add(2)
    linked_list.insert(0, 1)    # insert value 1 into index 0
    list_array = linked_list.to_array()
    assert_equal([1,2], list_array)

def test_remove():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    removed = linked_list.remove(1)

    assert_equal(removed.data, 2)
    assert_equal(removed.next_node, None)

    list_array = linked_list.to_array()
    assert_equal([1,3], list_array)

def test_remove_1():
    linked_list = LinkedList()
    linked_list.add(1)
    removed = linked_list.remove(0)

    assert_equal(removed.data, 1)
    assert_equal(removed.next_node, None)

    list_array = linked_list.to_array()
    assert_equal([], list_array)

def test_remove_2():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    removed = linked_list.remove(0)

    assert_equal(removed.data, 1)
    assert_equal(removed.next_node, None)

    list_array = linked_list.to_array()
    assert_equal([2], list_array)

def test_smallest():
    linked_list = LinkedList()
    linked_list.add(4)
    linked_list.add(5)
    linked_list.add(1)
    linked_list.add(3)
    linked_list.add(2)
    smallest_index = linked_list.smallest()
    assert_equal(smallest_index, 2)

def test_smallest_none():
    linked_list = LinkedList()
    smallest_index = linked_list.smallest()
    assert_equal(smallest_index, None)

def test_smallest_1():
    linked_list = LinkedList()
    linked_list.add(1)
    smallest_index = linked_list.smallest()
    assert_equal(smallest_index, 0)

def test_sort_desc():
    linked_list = LinkedList()
    linked_list.add(4)
    linked_list.add(1)
    linked_list.add(5)
    linked_list.add(3)
    linked_list.add(2)
    linked_list.sort_desc()
    list_array = linked_list.to_array()
    assert_equal([5,4,3,2,1], list_array)

def test_sort_desc():
    linked_list = LinkedList()
    linked_list.add(4)
    linked_list.add(1)
    linked_list.add(5)
    linked_list.add(3)
    linked_list.add(2)
    linked_list.sort_asc()
    list_array = linked_list.to_array()
    assert_equal([1,2,3,4,5], list_array)

def test_reverse():
    linked_list = LinkedList()
    linked_list.add(4)
    linked_list.add(1)
    linked_list.add(5)
    linked_list.add(3)
    linked_list.add(2)
    linked_list.reverse()
    list_array = linked_list.to_array()
    assert_equal([2,3,5,1,4], list_array)

def test_largest():
    linked_list = LinkedList()
    linked_list.add(4)
    linked_list.add(5)
    linked_list.add(1)
    linked_list.add(3)
    linked_list.add(2)
    largest_index = linked_list.largest()
    assert_equal(largest_index, 1)

def test_largest_none():
    linked_list = LinkedList()
    largest_index = linked_list.largest()
    assert_equal(largest_index, None)

def test_largest_1():
    linked_list = LinkedList()
    linked_list.add(1)
    largest_index = linked_list.largest()
    assert_equal(largest_index, 0)
