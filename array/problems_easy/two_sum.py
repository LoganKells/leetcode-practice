import numpy as np
import pytest


# See: https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = np.array(nums)
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            y_index = np.where(nums == y)[0]

            if y_index.size != 0:  # handle if y does not exist
                y_index = int(y_index[-1])  # handle if duplicate integers exist
                sum = x + y
                if sum == target and i != y_index:
                    return [i, y_index]


@pytest.mark.parametrize("test_input, target, expected", [([3, 2, 4], 6, [1, 2]),
                                                          ([2, 5, 5, 11], 10, [1, 2])])
def test_two_sum_1(test_input, target, expected):
    solution = Solution()
    return_values = solution.twoSum(nums=test_input, target=target)

    assert return_values == expected
