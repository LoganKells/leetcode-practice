import pytest
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Determine which list is shorter and longer
        max_nums = nums1 if len(nums1) >= len(nums2) else nums2
        min_nums = nums1 if len(nums1) < len(nums2) else nums2

        # Use a map to cache every number in min_nums
        map = {}
        for n in min_nums:
            if n in map.keys():
                map[n] += 1
            else:
                map[n] = 0

        # Evaluate where cached numbers show up in max_nums
        k = 0
        for n in max_nums:
            if n in map.keys() and map[n] >= 0:
                min_nums[k] = n  # save results in min_nums to save memory
                k += 1
                map[n] -= 1  # decrement cache count each time number is found equal between both lists

        intersection = min_nums[:k]
        intersection.sort()
        return intersection


test_cases = [([1, 2, 19, 200, 12, 2, 3, 4, 5, 0, 0, 9, 1, 2], [2, 2, 4, 5, 1, 23, 2, 56, 3, 19, 200],
               [1, 2, 2, 2, 3, 4, 5, 19, 200]),
              ([1, 2, 2, 1], [2, 2], [2, 2]),
              ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9])
              ]


@pytest.mark.parametrize("nums1, nums2, expected", test_cases)
def test_intersection(nums1, nums2, expected):
    sol = Solution()
    intersection = sol.intersect(nums1=nums1, nums2=nums2)
    assert intersection == expected
