from typing import List
import numpy as np
import pytest


# See: https://leetcode.com/problems/two-sum/

class SolutionNumpy(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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


class SolutionFastMap(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dynamic (hash)

        # Build a map of each value to it's index
        map = {}
        for idx_x, x in enumerate(nums):
            map[x] = idx_x

        for idx_x, x in enumerate(nums):
            y = target - x
            idx_y = map[y] if y in map.keys() else None
            if idx_y is not None and idx_y != idx_x:
                return [idx_x, idx_y]


test_cases = [([3, 2, 4], 6, [1, 2]), ([2, 5, 5, 11], 10, [1, 2])]


@pytest.mark.parametrize("test_input, target, expected", test_cases)
def test_two_sum_numpy(test_input, target, expected):
    solution = SolutionNumpy()
    return_values = solution.twoSum(nums=test_input, target=target)

    assert return_values == expected

@pytest.mark.parametrize("test_input, target, expected", test_cases)
def test_two_sum_map(test_input, target, expected):
    solution = SolutionFastMap()
    return_values = solution.twoSum(nums=test_input, target=target)

    assert return_values == expected
