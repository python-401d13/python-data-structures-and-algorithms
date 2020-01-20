from repeated_word import repeated_word
import pytest


def test_repeated_word(lengthy):
    """
    The first repeated word is found in a lengthy string.
    """

    lengthy.replace('The', 'the')

    expected = 'the'
    actual = repeated_word(lengthy)
    assert actual == expected


def test_repeated_word_capital(lengthy):
    """
    The first repeated word is found in a lengthy string with a case-sensative string.
    """

    expected = 'the'
    actual = repeated_word(lengthy)
    assert actual == expected


def test_repeated_word_punctuation(lengthy):
    """
    The right first repeated word is found even with punctuation in the string.
    """

    lengthy.replace('the', 'the,')

    expected = 'the'
    actual = repeated_word(lengthy)
    assert actual == expected


def test_no_repeated_word():
    """
    Strings without a repeated word show a null return.
    """

    lengthy = 'The quick brown fox jumps over a lazy dog'

    expected = None
    actual = repeated_word(lengthy)
    assert actual == expected


# Fixtures


@pytest.fixture
def lengthy():
    string = 'The quick brown fox jumps over the lazy dog'
    return string
