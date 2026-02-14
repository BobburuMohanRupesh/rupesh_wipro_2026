import pytest

def add(a, b):
    return a + b

# Q1: Parameterization
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (-1, 1, 0),
        (10, 20, 30)
    ]
)
def test_addition(a, b, expected):
    assert add(a, b) == expected
