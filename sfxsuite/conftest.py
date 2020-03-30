import pytest


@pytest.fixture()
def get_some_test_data():
    return [(3, 5, 8), (1, 2, 3), (10, 11, 21), (-10, -20, -30)]
