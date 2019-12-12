import importlib
import pytest
from linked_list import LinkedList, Node, RangeException

importlib.import_module('ll_merge', package='ll_merge')

# Fixtures


@pytest.fixture
def simple_ll():
    """Helper function to return a simple linked list with nodes."""

    linked_list = LinkedList()
    values = [5, 3, 2]
    for value in values:
        linked_list.insert(value)
    return linked_list


# Passing tests


def test_create_linked_list():
    """Test a linked list can be made."""

    linked_list = LinkedList()
    # Note: I found out about the built-in `vars` function on StackOverflow
    # Source: https://stackoverflow.com/questions/109087/how-to-get-instance-variables-in-python
    keys = vars(linked_list).keys()
    assert len(keys) == 1 and "head" in keys
    assert linked_list.head == None


def test_create_node():
    """Test a node can be made."""

    value = 1
    node = Node(value)
    assert node.value == value
    assert node.next == None


def test_insert_linked_list_node():
    """Test a node can be inserted at the head of the linked list."""

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
    """Test a linked list can be checked for the inclusion of a value."""

    value = 1
    linked_list = LinkedList()
    linked_list.insert(value)
    assert linked_list.includes(value)


def test_get_linked_list_values():
    """Test a linked list can be represented as a string."""

    linked_list = LinkedList()
    for i in range(3):
        value = i
        linked_list.insert(value)

    expected = "2, 1, 0"
    actual = str(linked_list)
    assert actual == expected


def test_linked_list_append():
    """Test a value can be appended to a linked list."""

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
    """Test a new value can be inserted before a value already in the linked list."""

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
    """Test a value can be inserted after a value already in the linked list."""

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


def test_kth_from_end_ll_middle(simple_ll):
    """Test the kth from the end value can be found in the middle of the linked list."""

    k = 1
    expected = 3
    actual = simple_ll.kth_from_end(k)
    assert actual == expected

# Failing tests


def test_linked_list_not_includes_value():
    """Test a linked list can be checked for the exclusion of a value."""

    value = 1
    linked_list = LinkedList()
    linked_list.insert(value)

    value = 2
    assert not linked_list.includes(value)


# Edge case tests


def test_kth_from_end_k_range_exception(simple_ll):
    """Test a linked list to return an exception when the `kth_from_end` method searches outside the size of the number of linked list nodes."""

    k = 6
    expected = str(RangeException("k not in range"))
    actual = str(simple_ll.kth_from_end(k))
    assert actual == expected


def test_kth_from_end_ll_k_same_length(simple_ll):
    """Test the linked list returns a range expection for the kth value from the end of the linked list where k is the size of the linked list."""

    k = 3
    expected = str(RangeException("k not in range"))
    actual = str(simple_ll.kth_from_end(k))
    assert actual == expected


def test_kth_from_end_negative_integer(simple_ll):
    """Test a linked list to return a value for negative integers searches of k where the absolute value of k is equal of less than the length of the linked list."""

    k = -1
    expected = 2
    actual = simple_ll.kth_from_end(k)
    assert actual == expected


def test_kth_from_end_ll_size_1():
    """Test a linked list to return the kth from the end value when the linked list has only one node."""

    k = 0
    linked_list = LinkedList()
    value = 1
    linked_list.insert(value)

    expected = value
    actual = linked_list.kth_from_end(k)
    assert actual == expected


def test_merge_list_empty_first_list():
    """Test correct return of two linked lists being merged with empty first linked list."""

    ll_one = LinkedList()
    ll_two = LinkedList()
    value = 1
    ll_two.insert(value)

    merged_ll = merge_lists(ll_one, ll_two)
    assert merged_ll.head.value == 1
    assert merged_ll.head.next == None
