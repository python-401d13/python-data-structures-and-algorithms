from challenges.fizzbuzz_tree.fizzbuzz_tree import fizzbuzz_tree
from challenges.tree.tree import BinarySearchTree
import pytest


def test_empty(binary_search_tree):
    """Trying to fizzbuzz an empty tree should return an empty tree."""

    expected = None
    actual = fizzbuzz_tree(binary_search_tree)
    assert actual == expected


def test_not_empty(binary_search_tree):
    """Fizzbuzz map the values of a tree."""

    values = [17, 11, 21, 3, 15, 25]
    for value in values:
        binary_search_tree.add(value)

    expected = ['Fizz', '11', 'FizzBuzz', '17', 'Fizz', 'Buzz']
    fizzbuzzed_tree = fizzbuzz_tree(binary_search_tree)
    actual = fizzbuzzed_tree.in_order(fizzbuzzed_tree._root)
    assert actual == expected


# Fixtures


@pytest.fixture
def binary_search_tree():
    return BinarySearchTree()
