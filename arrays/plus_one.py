from typing import List
import pytest

# 66. Plus One
# see - https://leetcode.com/problems/plus-one/


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # If the last digit is a 9, then we need to add an element
        # e.g.
        # [9] + 1 = [1, 0]
        # [1, 9] + 1 = [2, 0]
        # [1, 1, 9] + 1 = [1, 2, 0]
        # [1, 9, 9] + 1 = [2, 0, 0]
        # [9, 9, 9] + 1 = [1, 0, 0, 0]
        # [1, 8, 9, 9] + 1 = [1, 9, 0, 0]

        carryover = digits[-1] - 8
        i = len(digits) - 1
        while carryover > 0:
            digits[i] = 0
            i -= 1
            carryover = digits[i] - 8

        # Once the carryover is complete, add +1 to the ending index value.
        # If the ending index is -1, then we have to add a new element to the list.
        if i >= 0:
            digits[i] += 1
        else:
            digits.append(0)
            digits[0] = 1
        return digits


test_cases = [([9, 9, 9], [1, 0, 0, 0]),
              ([1, 8, 9, 9], [1, 9, 0, 0]),
              ([8, 9, 9], [9, 0, 0]),
              ([1, 9, 9], [2, 0, 0]),
              ([1, 1, 9], [1, 2, 0]),
              ([1, 9], [2, 0]),
              ([9], [1, 0]),
              ([1, 2, 3], [1, 2, 4]),
              ([4, 3, 2, 1], [4, 3, 2, 2]),
              ([0], [1])]


@pytest.mark.parametrize("nums, expected", test_cases)
def test_plus_one(nums, expected):
    sol = Solution()
    digits_plus_one = sol.plusOne(digits=nums)
    assert digits_plus_one == expected
