import functools
import pytest


@functools.cache
def fibonacci(n: int) -> int:
    # base case
    if n < 2:
        return n

    # Recursion
    return fibonacci(n - 2) + fibonacci(n - 1)


@pytest.mark.parametrize("test_input, expected", [(2, 1), (3, 2), (10, 55), (20, 6765)])
def test_fibonacci(test_input, expected):
    value = fibonacci(n=test_input)

    assert value == expected
