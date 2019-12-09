import pytest
from linked_list import LinkedList, Node

# Fixtures

# Passing tests


def test_create_linked_list():
    linked_list = LinkedList()
    # Note: I found out about the built-in `vars` function on StackOverflow
    # Source: https://stackoverflow.com/questions/109087/how-to-get-instance-variables-in-python
    keys = vars(linked_list).keys()
    assert len(keys) == 1 and "head" in keys
    assert linked_list.head == None


def test_create_node():
    value = 1
    node = Node(value)
    assert node.value == value
    assert node.next == None


def test_insert_linked_list_node():
    value = 1
    linked_list = LinkedList()
    linked_list.insert(value)
    assert linked_list.head.value == value
    assert linked_list.head.next == None

    value = 2
    linked_list.insert(value)
    assert linked_list.head.value == 2
    assert isinstance(linked_list.head.next, Node)
    assert linked_list.head.next.value == 1
    assert linked_list.head.next.next == None


def test_linked_list_includes_value():
    value = 1
    linked_list = LinkedList()
    linked_list.insert(value)
    assert linked_list.includes(value)


def test_get_linked_list_values():
    linked_list = LinkedList()
    for i in range(3):
        value = i
        linked_list.insert(value)

    expected = "2, 1, 0"
    actual = str(linked_list)
    assert actual == expected


def test_linked_list_append():
    linked_list = LinkedList()
    value = 1
    linked_list.insert(value)

    value = 2
    linked_list.append(value)
    assert linked_list.head.next.value == value
    assert linked_list.head.next.next == None

    value = 3
    linked_list.append(value)
    assert linked_list.head.next.next.value == value
    assert linked_list.head.next.next.next == None


def test_linked_list_insert_before():
    linked_list = LinkedList()
    value = 1
    linked_list.insert(value)

    new_value = 2
    linked_list.insert_before(value, new_value)
    assert linked_list.head.value == new_value
    assert linked_list.head.next.value == value

    newer_value = 3
    linked_list.insert_before(value, newer_value)
    assert linked_list.head.next.value == newer_value
    assert linked_list.head.next.next.value == value


def test_linked_list_insert_after():
    linked_list = LinkedList()
    value = 1
    linked_list.insert(value)

    new_value = 2
    linked_list.insert_after(value, new_value)
    assert linked_list.head.next.value == new_value
    assert linked_list.head.next.next == None

    newer_value = 3
    linked_list.insert_after(value, newer_value)
    assert linked_list.head.next.value == newer_value
    assert linked_list.head.next.next.value == new_value
    assert linked_list.head.next.next.next == None


# Failing tests


def test_linked_list_not_includes_value():
    value = 1
    linked_list = LinkedList()
    linked_list.insert(value)

    value = 2
    assert not linked_list.includes(value)


def test_not_get_linked_list_values():
    linked_list = LinkedList()
    for i in range(3):
        value = i
        linked_list.insert(value)

    expected = "0, 1, 2"
    actual = str(linked_list)
    assert not actual == expected


# Edge case tests
