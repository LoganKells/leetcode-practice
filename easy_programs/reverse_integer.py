# see: https://leetcode.com/problems/reverse-integer/
# solution: https://www.youtube.com/watch?v=HAgLH58IgJQ&t=11s
import math

# Define the max and min 32 bit signed integer
MAX_INT = 2 ** 31 - 1
MIN_INT = -1 * 2 ** 31

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # Reverse
        x_reversed = 0
        while abs(x) > 0:
            residual = int(math.fmod(x, 10))

            # Handle values above limit
            if x_reversed > MAX_INT // 10:
                return 0
            elif x_reversed < MIN_INT // 10:
                return 0
            elif x_reversed == MAX_INT // 10 and residual >= MAX_INT % 10:
                # If the x_reversed will overflow MAX_INT with next residual added to last digit place.
                return 0
            elif x_reversed == MIN_INT // 10 and residual <= MIN_INT % 10:
                # If the x_reversed will overflow MIN_INT with next residual added to last digit place.
                return 0
            else:
                # Reverse the integer (123 -> 321)
                x_reversed = (x_reversed * 10) + residual

            # loop condition, drop one element from the input integer, x
            x_str = str(x)
            x_str = x_str[:-1]
            if x_str not in ('-', ""):
                x = int(x_str)
            else:
                x = 0

        return x_reversed


def test_reverse_1():
    sol = Solution()
    reversed_int = sol.reverse(x=123)

    assert reversed_int == 321


def test_reverse_2():
    sol = Solution()
    reversed_int = sol.reverse(x=MAX_INT)

    assert reversed_int == 0


def test_reverse_3():
    sol = Solution()
    reversed_int = sol.reverse(x=-123)

    assert reversed_int == -321

