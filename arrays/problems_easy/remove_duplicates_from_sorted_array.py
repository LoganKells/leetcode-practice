from typing import List
import pytest


class Solution:
    def removeDuplicates(self, nums: List[int]):
        for i in range(len(nums) - 1):
            if i < len(nums) - 1:
                cursor = nums[i]
                first = nums[i + 1]

                while first == cursor:
                    nums.pop(i)
                    cursor = nums[i]
                    first = nums[i + 1] if i < len(nums) - 1 else None
            else:
                break
        return nums


test_cases = [([1, 1], [1]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]), ([1, 1, 2], [1, 2])]


@pytest.mark.parametrize("nums, expected", test_cases)
def test_remove_duplicates(nums, expected):
    solution = Solution()
    nums_no_dupicates = solution.removeDuplicates(nums=nums)

    assert nums_no_dupicates == expected
