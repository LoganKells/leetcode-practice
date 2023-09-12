import pytest
from typing import List


class Solution:
    def find_peak_length(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        peak_length = 0

        # Sort and pop the maximum value from the list
        arr.sort()
        peak_max = arr.pop()  # This is the intersecting peak from the increase -> peak -> decrease
        peak_length += 1  # Peak only counts once (intersecting peak)

        # Remove duplicates of the peak_max
        last_val = arr[-1] if len(arr) > 0 else -1  # handle if popping results in empty array.
        while last_val == peak_max:
            arr.pop()
            last_val = arr[-1] if len(arr) > 0 else -1  # handle if popping results in empty array.

        # Create a map of the unique values.
        # Add unique remaining values count to the peak length;
        # because the peak is strictly increasing on the left and right
        map = {}
        for i, num in enumerate(arr):
            map[num] = i
        peak_length += len(map.keys())

        # Handle the case when the absolute peak has equivalent values on the left and right side
        if len(map.keys()) != len(arr):
            peak_length += 1

        return peak_length


test_cases = [([4, 4, 2], 2),
              ([4, 5, 6, 3, 2], 5),
              ([2, 3, 3, 2, 2, 2, 1], 4),
              ([4, 5, 7, 6, 3, 2], 6),
              ([1, 2], 2),
              ([4, 4], 1),
              ([2, 5, 3, 2, 4, 1], 6),
              ([1], 1)
              ]


@pytest.mark.parametrize("nums, expected", test_cases)
def test_peak_length(nums, expected):
    sol = Solution()
    peak_length = sol.find_peak_length(arr=nums)

    assert peak_length == expected
