from tree_intersection import Node, BinaryTree, tree_intersection, walk
import pytest


@pytest.mark.parametrize('values_a, values_b, expected', [
    ((1, 2, 4, 5, 6, 8), (10, 2, 4, 15, 16, 8), {2, 4, 8}),
    ((1, 2, 4, 5, 6, 8), (10, 12, 14, 15, 16, 18), set({})),
    ((1, 2, 4, 5, 6, 8), tuple([]), set({})),
    (tuple([]), tuple([]), set({}))
])
def test_tree_intersection(values_a, values_b, expected):
    """
    The intersection of two trees is found.
    """

    # Write add method for BinaryTree
    tree_a = BinaryTree()
    if len(values_a) == 6:
        tree_a.root = Node(values_a[0])
        tree_a.root.left = Node(values_a[1])
        tree_a.root.right = Node(values_a[2])
        tree_a.root.left.left = Node(values_a[3])
        tree_a.root.left.right = Node(values_a[4])
        tree_a.root.right.right = Node(values_a[5])

    # Write add method for BinaryTree
    tree_b = BinaryTree()
    if len(values_b) == 6:
        tree_b.root = Node(values_b[0])
        tree_b.root.left = Node(values_b[1])
        tree_b.root.right = Node(values_b[2])
        tree_b.root.left.left = Node(values_b[3])
        tree_b.root.left.right = Node(values_b[4])
        tree_b.root.right.right = Node(values_b[5])

    actual = tree_intersection(tree_a, tree_b)
    assert actual == expected
