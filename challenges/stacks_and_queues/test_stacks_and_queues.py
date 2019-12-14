import pytest
from stacks_and_queues import (
    Node,
    Queue,
    Stack,
    EmptyQueueException,
    EmptyStackException,
)


# Node tests


@pytest.mark.parametrize("value", [("Python")])
def test_create_node(value):
    """A Stack and Queue node can be created."""

    node = Node(value)
    assert node.value == value
    assert node.next == None


# Stack tests


def test_create_stack(stack):
    """A Stack can be created."""

    assert stack.top == None


@pytest.mark.parametrize("value_a", [("Python")])
def test_stack_push_while_empty(stack, value_a):
    """A node can be added to an empty stack."""

    stack.push(value_a)
    assert stack.top.value == value_a
    assert stack.top.next == None


@pytest.mark.parametrize("value_a,value_b", [("Python", "Language")])
def test_stack_push_while_not_empty(stack, value_a, value_b):
    """A node can be added to a non-empty stack."""

    stack.push(value_a)
    stack.push(value_b)
    assert stack.top.value == value_b
    assert isinstance(stack.top.next, Node)
    assert stack.top.next.value == value_a
    assert stack.top.next.next == None


def test_stack_is_empty_while_empty(stack):
    """A stack is empty."""

    assert stack.is_empty() == True


@pytest.mark.parametrize("value", [("Python")])
def test_stack_is_empty_while_not_empty(stack, value):
    """A stack isn't empty."""

    stack.push(value)
    assert stack.is_empty() == False


def test_stack_pop_while_empty(stack):
    """Removing from an empty stack returns an exception."""

    try:
        stack.pop()
    except EmptyStackException:
        assert True


@pytest.mark.parametrize("value", [("Python")])
def test_stack_pop_while_not_empty(stack, value):
    """Remove node from a non-empty stack."""

    stack.push(value)
    node_value = stack.pop()
    assert value == node_value
    assert stack.top == None

@pytest.mark.parametrize("value_a,value_b", [("Python", "Language")])
def test_stack_pop_until_empty(stack, value_a, value_b):
    """Pop a stack until empty."""

    stack.push(value_a)
    stack.push(value_b)
    stack.pop()
    stack.pop()
    assert stack.top == None


def test_stack_peek_while_empty(stack):
    """Can't see the top value of a stack with no values."""

    try:
        stack.peek()
    except EmptyStackException:
        assert True


@pytest.mark.parametrize("value", [("Python")])
def test_stack_peek_while_not_empty(stack, value):
    """See the top value of a stack."""

    stack.push(value)
    node_value = stack.peek()
    assert value == node_value


# Queue tests


def test_create_queue(queue):
    """A Queue can be created."""

    assert queue.front == None
    assert queue.rear == None


@pytest.mark.parametrize("value", [("Python")])
def test_queue_enqueue_while_empty(queue, value):
    """Add to an empty queue."""

    queue.enqueue(value)
    assert queue.front.value == value
    assert queue.front.next == None
    assert queue.rear.value == value
    assert queue.rear.next == None


@pytest.mark.parametrize("value_a,value_b", [("Python", "Language")])
def test_queue_enqueue_while_one_node(queue, value_a, value_b):
    """Add to a queue with one node."""

    queue.enqueue(value_a)
    queue.enqueue(value_b)
    assert queue.front.value == value_a
    assert isinstance(queue.front.next, Node)
    assert queue.rear.value == value_b
    assert queue.rear.next == None


@pytest.mark.parametrize("value_a,value_b,value_c", [("Python", "Language", "Shell")])
def test_queue_enqueue_while_two_node(queue, value_a, value_b, value_c):
    """Add to a queue with two nodes."""

    queue.enqueue(value_a)
    queue.enqueue(value_b)
    queue.enqueue(value_c)

    assert queue.front.value == value_a
    assert isinstance(queue.front.next, Node)
    assert queue.rear.value == value_c
    assert queue.rear.next == None


def test_queue_is_empty_while_empty(queue):
    """An empty queue is empty."""

    assert queue.is_empty()


@pytest.mark.parametrize("value", [("Python")])
def test_queue_is_empty_while_not_empty(queue, value):
    """A non-empty queue isn't empty."""

    queue.enqueue(value)
    assert not queue.is_empty()


def test_queue_dequeue_while_empty(queue):
    """Can't remove from an empty queue."""

    try:
        queue.dequeue()
    except EmptyQueueException:
        assert True


@pytest.mark.parametrize("value", [("Python")])
def test_queue_dequeue_with_one_node(queue, value):
    """Remove from a queue with one node."""

    queue.enqueue(value)
    node_value = queue.dequeue()
    assert node_value == value
    assert queue.front == None
    assert queue.rear == None


@pytest.mark.parametrize("value_a,value_b", [("Python", "Language")])
def test_queue_dequeue_with_two_nodes(queue, value_a, value_b):
    """Remove from a queue with two nodes."""

    queue.enqueue(value_a)
    queue.enqueue(value_b)
    node_value = queue.dequeue()
    assert node_value == value_a
    assert queue.front.value == value_b
    assert queue.front.next == None
    assert queue.rear.value == value_b
    assert queue.rear.next == None

@pytest.mark.parametrize("value_a,value_b", [("Python", "Language")])
def test_queue_dequeue_until_empty(queue, value_a, value_b):
    """Remove from a queue until empty."""

    queue.enqueue(value_a)
    queue.enqueue(value_b)
    queue.dequeue()
    queue.dequeue()
    assert queue.front == None
    assert queue.rear == None

def test_queue_peek_while_empty(queue):
    """An empty queue has no value."""

    try:
        queue.peek()
    except EmptyQueueException:
        assert True


@pytest.mark.parametrize("value", [("Python")])
def test_queue_peek_while_not_empty(queue, value):
    """A non-empty queue has a value at the front."""

    queue.enqueue(value)
    node_value = queue.peek()
    assert node_value == value


# Fixtures


@pytest.fixture
def stack():
    """Return a Stack instance for testing."""

    return Stack()


@pytest.fixture
def queue():
    """Return a Queue instnace for testing."""

    return Queue()
