import pytest

# see - https://leetcode.com/problems/powx-n/

class SolutionSlowIterative:
    def myPow(self, x: float, n: int) -> float:
        # Iterative, slow
        if n == 0:
            return 1

        value = 1
        for i in range(abs(n)):
            if n < 0:
                value /= x
            else:
                value *= x
        return value


class SolutionFastRecursive:
    def fast_power(self, x: float, n: int) -> float:
        # Recursive, fast
        if int(n) == 0:
            return 1.0
        half_power_result = self.fast_power(x, int(n / 2))

        if abs(half_power_result) < 1e-5:
            return 0.0
        elif n % 2 == 0:
            return half_power_result * half_power_result
        else:
            return half_power_result * half_power_result * x

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n *= -1

        return self.fast_power(x, n)


test_cases = [(-2.0, 2, 4.0), (0.00001, 214748364, 0.0), (2.0, 10, 1024.0), (2.0, 3, 8.0)]


@pytest.mark.parametrize("x, n, expected", test_cases)
def test_power_fast_recursive(x, n, expected):
    power = SolutionFastRecursive()
    power_result = power.myPow(x, n)

    assert power_result == expected


@pytest.mark.parametrize("x, n, expected", test_cases)
def test_power_fast_recursive(x, n, expected):
    power = SolutionSlowIterative()
    power_result = power.myPow(x, n)

    assert power_result == expected
