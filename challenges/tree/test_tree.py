import pytest
from tree import BinarySearchTree, BinaryTree, _Node
from challenges.stacks_and_queues.stacks_and_queues import Queue, EmptyQueueException


def test_create_node():
    """A protected Node should be created."""

    value = 11
    node = _Node(11)
    assert node.value == value
    assert node.left == None
    assert node.right == None


def test_create_binary_tree():
    """A Binary Tree should be created."""

    binary_tree = BinaryTree()
    assert binary_tree._root == None


def test_create_binary_search_tree():
    """A Binary Search Tree should be created."""

    binary_search_tree = BinarySearchTree()
    assert binary_search_tree._root == None


def test_bst_add_when_no_root(binary_search_tree):
    """Add a value to a Binary Search Tree."""

    expected = 11
    binary_search_tree.add(expected)
    actual = binary_search_tree._root.value
    assert actual == expected


def test_bst_add_when_root_and_no_left(binary_search_tree):
    """Add a value to a Binary Search Tree with a root and no left branch."""

    value = 11
    expected = 7
    binary_search_tree.add(value)
    binary_search_tree.add(expected)

    actual = binary_search_tree._root.left.value
    assert actual == expected


def test_bst_add_when_root_and_left(binary_search_tree):
    """Add a value to a Binary Search Tree a root and a left branch."""

    values = [11, 7]
    expected = 3
    for value in values:
        binary_search_tree.add(value)
    binary_search_tree.add(expected)

    actual = binary_search_tree._root.left.left.value
    assert actual == expected


def test_pre_order(binary_search_tree):
    """See the values of the pre-order walk of a Binary Tree."""

    values = [11, 7, 3, 9, 19, 15]
    for value in values:
        binary_search_tree.add(value)

    expected = values
    actual = binary_search_tree.pre_order(binary_search_tree._root)
    assert actual == expected


def test_in_order(binary_search_tree):
    """See the values of the in-order walk of a Binary Tree."""

    values = [11, 7, 3, 9, 19, 15]
    for value in values:
        binary_search_tree.add(value)

    expected = [3, 7, 9, 11, 15, 19]
    actual = binary_search_tree.in_order(binary_search_tree._root)
    assert actual == expected


def test_post_order(binary_search_tree):
    """See the values of the post-order walk of a Binary Tree."""

    values = [11, 7, 3, 9, 19, 15]
    for value in values:
        binary_search_tree.add(value)

    expected = [3, 9, 7, 15, 19, 11]
    actual = binary_search_tree.post_order(binary_search_tree._root)
    assert actual == expected


def test_bst_contains(binary_search_tree):
    """Check a value is in a binary search tree."""

    values = [11, 7, 3, 9, 19, 15]
    for value in values:
        binary_search_tree.add(value)

    expected = True
    actual = binary_search_tree.contains(3)
    assert actual == expected


def test_bst_not_contains(binary_search_tree):
    """Check a value is in a binary search tree when not in the binary search tree."""

    values = [11, 7, 3, 9, 19, 15]
    for value in values:
        binary_search_tree.add(value)

    expected = False
    actual = binary_search_tree.contains(16)
    assert actual == expected


def test_breadth_first_search_empty(binary_tree):
    """A list of all values of an empty Binary Tree instance should be an empty list"""

    expected = []
    actual = binary_tree.breadth_first_search()
    assert actual == expected


def test_breadth_first_search_not_empty(binary_tree):
    """A list of values in breadth-first order of a Binary Tree instance"""

    binary_tree._root = _Node(5)
    binary_tree._root.left = _Node(3)
    binary_tree._root.right = _Node(1)
    binary_tree._root.left.left = _Node(8)
    binary_tree._root.left.right = _Node(6)
    binary_tree._root.right.right = _Node(4)

    expected = [5, 3, 1, 8, 6, 4]
    actual = binary_tree.breadth_first_search()
    assert actual == expected


def test_find_maximum_value_empty(binary_tree):
    """The maximum of an empty tree should be None."""

    expected = None
    actual = binary_tree.find_maximum_value(binary_tree._root)
    assert actual == expected


def test_find_maximum_value_single_node(binary_tree):
    """The maximum of a single-node tree should be the value of the root."""

    expected = 2
    binary_tree._root = _Node(expected)

    actual = binary_tree.find_maximum_value(binary_tree._root)
    assert actual == expected


def test_find_maximum_value_multi_node(binary_tree):
    """The maximum of a multi-node tree should the maximum value of the tree."""

    maximum = 19
    binary_tree._root = _Node(2)
    binary_tree._root.left = _Node(15)
    binary_tree._root.right = _Node(11)
    binary_tree._root.left.left = _Node(7)
    binary_tree._root.left.right = _Node(maximum)
    binary_tree._root.right.left = _Node(4)
    binary_tree._root.right.right = _Node(3)

    actual = binary_tree.find_maximum_value(binary_tree._root)
    assert actual == maximum


# Fixtures


@pytest.fixture
def binary_tree():
    """Create a Binary Tree."""

    return BinaryTree()


@pytest.fixture
def binary_search_tree():
    """Create a Binary Search Tree."""

    return BinarySearchTree()
