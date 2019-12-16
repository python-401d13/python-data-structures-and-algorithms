from challenges.stacks_and_queues.stacks_and_queues import EmptyQueueException, EmptyStackException, Node, Stack

class PseudoQueue:
    """Queue data structure made with Stack data structure under the hood."""

    def __init__(self):
        """PseudoQueue constructor."""

        self.stack_one = Stack()
        self.stack_two = Stack()
        self.size = 0

    def enqueue(self, value):
        """Add a value to the rear of the pseudo queue."""

        for _ in range(self.size):
            node_value = self.stack_one.pop()
            self.stack_two.push(node_value)

        self.stack_two.push(value)
        self.size += 1

        for _ in range(self.size):
            node_value = self.stack_two.pop()
            self.stack_one.push(node_value)

    def dequeue(self):
        """Remove a value from the front of the pseudo queue."""

        if not self.size:
            return EmptyQueueException()

        return self.stack_one.pop()

    def peek(self):
        """See the pseudo front queue value."""

        return self.stack_one.peek()
