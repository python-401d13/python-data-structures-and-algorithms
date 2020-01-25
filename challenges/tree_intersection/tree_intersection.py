
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None


def tree_intersection(tree_a, tree_b):
    """
    Find the intersection of values in two trees.
    """

    union = set({})
    intersection = set({})
    root_a = tree_a.root
    root_b = tree_b.root

    if not root_a or not root_b:
        return intersection

    walk(root_a, union, intersection)
    walk(root_b, union, intersection)

    return intersection


def walk(root, union, intersection):
    """
    In-order walk a tree adding to sets union and intersection.
    """

    if root.left:
        walk(root.left, union, intersection)

    if root.value in union:
        intersection.add(root.value)
    else:
        union.add(root.value)

    if root.right:
        walk(root.right, union, intersection)
