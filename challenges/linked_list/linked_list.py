class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        list_str = ""
        current = self.head
        while current:
            list_str += str(current.value)
            if current.next:
                list_str += ", "
            current = current.next
        return list_str

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next

        return False


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
