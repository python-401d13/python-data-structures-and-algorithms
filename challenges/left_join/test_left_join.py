from left_join import left_join
import pytest


@pytest.mark.parametrize('hash_one, hash_two, expected', [
    ({
        'fond': 'enamored',
        'wrath': 'anger',
        'diligent': 'employed',
        'outfit': 'garb',
        'guide': 'usher',
    }, {
        'fond': 'averse',
        'wrath': 'delight',
        'diligent': 'idle',
        'guide': 'follow',
        'flow': 'jam',
    }, {
        'fond': ['enamored', 'averse'],
        'wrath': ['anger', 'delight'],
        'diligent': ['employed', 'idle'],
        'outfit': ['garb', None],
        'guide': ['usher', 'follow'],
    }),


    ({
        'fond': 'enamored',
        'wrath': 'anger',
        'diligent': 'employed',
        'outfit': 'garb',
        'guide': 'usher',
    },
    {},
    {
        'fond': ['enamored', None],
        'wrath': ['anger', None],
        'diligent': ['employed', None],
        'outfit': ['garb', None],
        'guide': ['usher', None],
    }),


    ({},
    {
        'fond': 'averse',
        'wrath': 'delight',
        'diligent': 'idle',
        'guide': 'follow',
        'flow': 'jam',
    },
    {}),


    ({}, {}, {})
])
def test_left_join(hash_one, hash_two, expected):
    """
    Two hashmaps can be left joined.
    """

    actual = left_join(hash_one, hash_two)
    assert actual == expected
