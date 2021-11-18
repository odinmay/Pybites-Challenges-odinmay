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

@pytest.mark.parametrize("nums", [
    ([1, 2, -5]),
    ([-1, 2, 5]),
    ([11, 2, 5]),
    ([10, 5, 2]),
])
def test_value_errors(nums):
    with pytest.raises(ValueError):
        list_to_decimal(nums)

@pytest.mark.parametrize("nums", [
    ([1.5, 4, 6]),
    ([5, 5.2, 7]),
    ([1, 3, True]),
    (['1', 4, 6]),
    ([6, 1, False]),
    (["4", 5, 4])
])
def test_type_errors(nums):
    with pytest.raises(TypeError):
        list_to_decimal(nums)
