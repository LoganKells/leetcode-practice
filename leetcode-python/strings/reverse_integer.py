import pytest


class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -1 * 2 ** 31
        num = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        level = len(str(x))

        # Reverse one digit at a time, check if within signed 32-bit range
        for i in reversed(range(level)):
            res = x % 10
            if MIN_INT <= num + res * 10 ** i <= MAX_INT:
                num += res * 10 ** i
            else:
                return 0
            # num += res * 10 ** i

            # Update x
            x = (x - res) / 10
        return sign * int(num)


test_cases = [(1534236469, 0), (123, 321), (-123, -321), (120, 21), (0, 0)]


@pytest.mark.parametrize("x, expected", test_cases)
def test_reverse_x(x, expected):
    sol = Solution()
    x_reversed = sol.reverse(x=x)

    assert x_reversed == expected
