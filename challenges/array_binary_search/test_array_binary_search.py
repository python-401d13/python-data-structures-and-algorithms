import pytest
from array_binary_search import array_binary_search


def test_array_binary_search_in():
    expected = 1
    actual = array_binary_search([1, 2, 3], 2)
    assert actual == expected


def test_array_binary_search_not_in():
    expected = -1
    actual = array_binary_search([1, 2, 3], 4)
    assert actual == expected
