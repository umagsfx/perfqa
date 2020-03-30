import pytest


def sample(num1, num2):
    return num1 + num2


@pytest.mark.parametrize('num1, num2, expected', [(3, 5, 8), (4, 5, 9), (10, 11, 21), (-10, -20, -30)])
def test_param(num1, num2, expected):
    assert sample(num1, num2) == expected


def test_param_one(get_some_test_data):
    for item in get_some_test_data:
        num1 = item[0]
        num2 = item[1]
        expected = item[2]
        assert sample(num1, num2) == expected
