from challenges.stacks_and_queues.stacks_and_queues import Queue, EmptyQueueException


class _Node():
    """Protected Node which make branches and leafs of a Binary Tree."""

    def __init__(self, value):
        """Protected Node constructor."""

        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    """Binary Tree data structure."""

    def __init__(self, node=None):
        """Binary Tree constructor."""

        self._root = node

    def pre_order(self, node, order_list=[]):
        """See a pre-order list of Binary Tree values."""

        order_list.append(node.value)

        if node.left:
            self.pre_order(node.left, order_list)

        if node.right:
            self.pre_order(node.right, order_list)

        return order_list

    def in_order(self, node, order_list=[]):
        """See an in-order list of Binary Tree values."""

        if node.left:
            self.in_order(node.left, order_list)

        order_list.append(node.value)

        if node.right:
            self.in_order(node.right, order_list)

        return order_list

    def post_order(self, node, order_list=[]):
        """See a post-order list of Binary Tree values."""

        if node.left:
            self.post_order(node.left, order_list)

        if node.right:
            self.post_order(node.right, order_list)

        order_list.append(node.value)

        return order_list

    def breadth_first_search(self):
        """Return a list of all values of a binary tree in breadth-first order"""

        value_list = []

        if not self._root:
            return value_list

        queue = Queue()
        queue.enqueue(self._root)

        while not isinstance(queue.peek(), EmptyQueueException):
            node = queue.dequeue()
            value_list.append(node.value)

            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)

        return value_list


class BinarySearchTree(BinaryTree):
    """Binary Search Tree (BST) data structure."""

    def add(self, value):
        """
        Add a node to a Binary Search Tree.

        > Pair programmed
        > Driver: Ana Lebedeva
        > Navigator: Ethan Davis
        """

        node = _Node(value)

        if not self._root:
            self._root = node
            return

        current = self._root
        while True:
            if node.value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = node
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    return

    def contains(self, value):
        """Check a value is in a Binary Search Tree."""

        if not self._root:
            # TODO method should raise an exception
            return False

        current = self._root
        while True:
            if value == current.value:
                return True

            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    return False
            else:
                if current.right:
                    current = current.right
                else:
                    return False
