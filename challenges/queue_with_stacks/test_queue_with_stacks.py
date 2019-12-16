import pytest
from queue_with_stacks import PseudoQueue
from challenges.stacks_and_queues.stacks_and_queues import EmptyQueueException


def test_enqueue_when_empty(pseudo_queue):
    """Empty Pseudo Queue should add a value."""

    value = "Python"
    pseudo_queue.enqueue(value)
    assert pseudo_queue.peek() == value


def test_enqueue_when_not_empty(pseudo_queue):
    """Non-empty Pseudo Queue should add a value."""

    value_one = "Python"
    value_two = "Language"
    pseudo_queue.enqueue(value_one)
    pseudo_queue.enqueue(value_two)
    assert pseudo_queue.peek() == value_one


def test_dequeue_when_empty(pseudo_queue):
    """Empty Pseudo Queue can't remove a value."""

    assert isinstance(pseudo_queue.dequeue(), EmptyQueueException)


def test_dequeue_when_not_empty(pseudo_queue):
    """Non-empty Pseudo Queue should remove a value."""

    expected = "Python"
    pseudo_queue.enqueue(expected)
    actual = pseudo_queue.dequeue()
    assert actual == expected

# Fixtures


@pytest.fixture
def pseudo_queue():
    return PseudoQueue()
