class Node:
    """Node for links of a stack or queue."""

    def __init__(self, value):
        """Node constructor."""

        self.value = value
        self.next = None

class Stack:
    """Stack which holds a FILO list of nodes."""

    def __init__(self):
        """Stack constructor."""

        self.top = None

    def push(self, value):
        """Add node to Stack in O(1)."""

        tmp = self.top
        node = Node(value)
        self.top = node
        node.next = tmp

    def pop(self):
        """Remove node from Stack in O(1)."""

        if not self.top:
            raise EmptyStackException()

        tmp = self.top
        self.top = self.top.next
        tmp.next == None

        return tmp.value

    def peek(self):
        """See the value at the top of the stack in O(1)."""

        if not self.top:
            return EmptyStackException()

        return self.top.value

    def is_empty(self):
        """Does a stack have any nodes?"""

        return not self.top


class Queue():
    """Queue which holds FIFO list of nodes."""

    def __init__(self):
        """Queue constructor."""

        self.front = None
        self.rear = None

    def enqueue(self, value):
        """Add a value to the queue in O(1)."""

        node = Node(value)

        if not self.rear:
            self.front = node
            self.rear = node
            return

        tmp = self.rear
        self.rear = node
        tmp.next = node

    def dequeue(self):
        """Remove a value from a queue in O(1)."""

        if self.is_empty():
            raise EmptyQueueException()

        tmp = self.front

        if self.front.next == None:
            self.rear = None

        self.front = self.front.next
        tmp.next = None

        return tmp.value

    def peek(self):
        """See the value at the front of the queue."""

        if self.is_empty():
            raise EmptyQueueException()

        return self.front.value

    def is_empty(self):
        """Does a queue have any nodes?"""

        return not self.front and not self.rear

class EmptyStackException(Exception):
    """Exception returned when reading from an empty stack."""

    def __init__(self):
        """EmptyStackException constructor."""

        self.text = "Stack is empty"

class EmptyQueueException(Exception):
    """Exception returned when reading from an empty queue."""

    def __init__(self):
        """EmptyQueueException constructor."""

        self.text = "Queue is empty."
