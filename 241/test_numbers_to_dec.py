import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize("nums, expected", [
    ([0, 4, 2, 8], 428),
    ([1, 2], 12),
    ([3], 3),
    ([6, 2], 62),
    ([0, 0, 4, 0, 2], 402),
])
def test_list_to_decimal(nums, expected):
    assert list_to_decimal(nums) == expected


def test_bool_input():
    with pytest.raises(TypeError):
        list_to_decimal([1, 2 , True])

def test_float_input():
    with pytest.raises(TypeError):
        list_to_decimal([2.5, 4, 3, 6])

def test_string_input():
    with pytest.raises(TypeError):
        list_to_decimal([2, 2, '2'])

def test_negative():
    with pytest.raises(ValueError):
        list_to_decimal([-2, 4, 6, 7])

