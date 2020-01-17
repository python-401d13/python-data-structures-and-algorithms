from collections import deque

import pytest

from hashtable import Hashtable


def test_hash(hashtable):
    """
    Hash function gives expected values.
    """

    key = 'cat'

    expected = 8
    actual = hashtable.hash(key)

    assert actual == expected

    key = 'tac'

    actual = hashtable.hash(key)

    assert actual == expected


def test_add(hashtable):
    """
    Can add a key-value pair to a hashtable.
    """

    key = 'cat'
    value = 9
    hashtable.add(key, value)

    d = deque()
    d.append([key, value])

    expected = d[0]
    actual = hashtable.buckets[8][0]

    assert actual == expected


def test_add_collision(hashtable):
    """
    Can add a key-value pair to a hashtable with collision.
    """

    keys = ['cat', 'act']
    values = [9, 11]
    d = deque()
    for i in range(len(keys)):
        hashtable.add(keys[i], values[i])
        d.append([keys[i], values[i]])

        expected = d[i]
        actual = hashtable.buckets[8][i]

        assert actual == expected


def test_contains(hashtable):
    """
    Can check a hashtable for a key-value pair.
    """

    key = 'cat'
    value = 9
    hashtable.add(key, value)

    expected = True
    actual = hashtable.contains(key)

    assert actual == expected


def test_contains_collision(hashtable):
    """
    Can check a hashtable for a key-value pair with hashtable collision.
    """

    keys = ['cat', 'act']
    values = [9, 11]
    for i in range(len(keys)):
        hashtable.add(keys[i], values[i])

    expected = True
    actual = hashtable.contains(keys[1])

    assert actual == expected


def test_no_contains(hashtable):
    """
    Not all key-value pairs need to be in a hashtable.
    """

    key = 'cat'

    expected = False
    actual = hashtable.contains(key)

    assert actual == expected


def test_get(hashtable):
    """
    Can get a value from a hashtable.
    """

    key = 'cat'
    value = 9
    hashtable.add(key, value)

    expected = value
    actual = hashtable.get(key)

    assert actual == expected


def test_get_collision(hashtable):
    """
    Can get a value from a hashtable with a collision
    """

    keys = ['cat', 'act']
    values = [9, 11]
    for i in range(len(keys)):
        hashtable.add(keys[i], values[i])

    expected = values[1]
    actual = hashtable.get(keys[1])

    assert actual == expected


def test_no_get(hashtable):
    """
    Can't get a value from a hashtbale which isn't in the hashtable.
    """

    key = 'cat'

    expected = None
    actual = hashtable.get(key)

    assert actual == expected


# Fixtures


@pytest.fixture
def hashtable():
    """
    Hashtable instance.
    """

    return Hashtable()
