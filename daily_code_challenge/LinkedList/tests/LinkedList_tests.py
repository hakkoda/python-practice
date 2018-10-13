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
