from nose.tools import *
from Anagram.app import Anagram

def test_str_to_list():
    anagram = Anagram()
    word_list = anagram.str_to_list("abc")
    assert_equal(word_list, [ "a", "b", "c" ])

def test_sort_word():
    anagram = Anagram()
    sorted_word = anagram.sort_word("cba")
    assert_equal(sorted_word, [ "a", "b", "c" ])

def test_is_anagram_true():
    anagram = Anagram()
    is_anagram = anagram.is_anagram("abc", "cba")
    assert_equal(is_anagram, True)

def test_is_anagram_false():
    anagram = Anagram()
    is_anagram = anagram.is_anagram("abc", "def")
    assert_equal(is_anagram, False)

def test_is_anagram_false_different_lengths():
    anagram = Anagram()
    is_anagram = anagram.is_anagram("abcd", "cba")
    assert_equal(is_anagram, False)
