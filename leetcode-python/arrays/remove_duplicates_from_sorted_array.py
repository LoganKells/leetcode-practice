from typing import List
import pytest

# See - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# 2021-09-06
class Solution1:
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

# 2022-06-30
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = len(nums)
        j = 0
        i = 0
        final_size = 0
        while i < count - 1:
            if nums[i + 1] == nums[i]:
                i += 1
            else:
                j += 1
                i += 1
                final_size += 1
                nums[j] = nums[i]
        return j + 1

test_cases = [([1, 1], [1]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]), ([1, 1, 2], [1, 2])]


@pytest.mark.parametrize("nums, expected", test_cases)
def test_remove_duplicates(nums, expected):
    solution = Solution()
    nums_no_dupicates = solution.removeDuplicates(nums=nums)

    for i in range(nums_no_dupicates):
        assert nums[i] == expected[i]

