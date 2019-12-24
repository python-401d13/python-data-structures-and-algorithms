from challenges.tree.tree import BinaryTree, _Node


def fizzbuzz_tree(tree):
    """Take a tree tree and return a new tree with values fizzbuzzed."""

    if not tree._root:
        return None

    node = fizzbuzz_node(tree._root)
    new_tree = BinaryTree(node)
    return new_tree


def fizzbuzz_node(node):
    """Take a node and return a new node with the value fizzbuzzed."""

    new_node = _Node(node.value)
    if node.left:
        new_node.left = fizzbuzz_node(node.left)
    if node.right:
        new_node.right = fizzbuzz_node(node.right)

    new_node.value = fizzbuzz(new_node.value)

    return new_node


def fizzbuzz(value):
    """Return the fizzbuzz of a value."""

    if value % 3 == 0 and value % 5 == 0:
        return 'FizzBuzz'
    elif value % 3 == 0:
        return 'Fizz'
    elif value % 5 == 0:
        return 'Buzz'
    else:
        return str(value)
