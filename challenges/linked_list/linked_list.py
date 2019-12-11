class LinkedList:
    """Linked list data structure type."""

    def __init__(self):
        """Instance constructor."""

        self.head = None

    def __str__(self):
        """User facing string representation of a LinkedList instance."""

        list_str = ""
        current = self.head
        while current:
            list_str += str(current.value)
            if current.next:
                list_str += ", "
            current = current.next
        return list_str

    def insert(self, value):
        """
        Insert a value at the head of the linked list.

        Parameters:
        value (): Value to be in an node to insert into the linked list
        """

        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        """
        Check the linked list has a value in a node.

        Parameters:
        value (): Value to check for in the linked list

        Returns:
        boolean: Whether the value is in a node of the linked list
        """

        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def append(self, value):
        """
        Append a value in a new node to the end of a linked list instance with at least one node.

        Parameters:
        value (): Value to append to the end of a linked list instance.
        """

        current = self.head
        while current:
            if current.next == None:
                node = Node(value)
                current.next = node
                return
            current = current.next

    def insert_before(self, value, new_value):
        """
        Insert a value in a node in-front of a node with a different value already in the linked list.

        Parameters:
        value (): Old value in linked list to insert before
        new_value (): New value to insert into linked list
        """

        node = Node(new_value)

        if self.head and self.head.value == value:
            node.next = self.head
            self.head = node
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                node.next = current.next
                current.next = node
                break
            current = current.next

    def insert_after(self, value, new_value):
        """
        Insert a value in a node after a node with a different value already in the linked list.

        Parameters:
        value (): Old value in linked list to insert after
        new_value (): New value to insert into linked list
        """

        current = self.head
        while current:
            if current.value == value:
                node = Node(new_value)
                node.next = current.next
                current.next = node
                break
            current = current.next


    def kth_from_end(self, k):
        """
        Get the kth from the end node value in the linked list.

        Parameters:
        k (): How many nodes from the end of the linked list should be the node to return a value

        Returns:
        (): The value of the kth node from the end of the linked list
        """

        length = self._length()

        if not -length <= k < length:
            return RangeException('k not in range')

        step_count = None
        if k >= 0:
            step_count = length - k - 1
        if k < 0:
            step_count = abs(k) - 1

        current = self.head
        for i in range(step_count):
            current = current.next

        return current.value

    def _length(self):
        """
        Get the length of the linked list.

        Returns:
        int: Number of nodes in the linked list
        """

        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

class Node:
    """A linked list data structure node."""

    def __init__(self, value):
        """Instance constructor."""

        self.value = value
        self.next = None


class RangeException(Exception):
    """Exception which may be returned from `kth_from_end` instance method."""

    pass
