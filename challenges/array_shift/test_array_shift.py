from array_shift import insert_shift_array


def test_one():
    expected = [1, 2, 5, 3, 4]
    actual = insert_shift_array([1, 2, 3, 4], 5)
    assert actual == expected


def test_two():
    expected = [1, 2, 3, 6, 4, 5]
    actual = insert_shift_array([1, 2, 3, 4, 5], 6)
    assert actual == expected


def test_three():
    expected = [1, 2, 3]
    actual = insert_shift_array([1, 4, 2, 3], 4)
    assert actual != expected


def test_four():
    expected = [1]
    actual = insert_shift_array([], 1)
    assert actual == expected


def test_five():
    expected = [1, 2]
    actual = insert_shift_array([1], 2)
    assert actual == expected
