from typing import List
import pytest

# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Copy the values from nums1, because we're overriding nums1 with new values in a loop.
        values_nums1 = nums1[:m]

        # Initialize cursors at the beginning of both lists.
        i = 0
        c1 = 0
        c2 = 0

        # Sort using a cursor
        while c1 < m and c2 < n:

            n1 = values_nums1[c1]
            n2 = nums2[c2]

            if n1 <= n2:
                nums1[i] = n1
                c1 += 1
            else:
                nums1[i] = n2
                c2 += 1
            i += 1

        # If any values remain in a list, then append
        while c2 < n:
            n2 = nums2[c2]
            nums1[i] = n2
            c2 += 1
            i += 1
        while c1 < m:
            n1 = values_nums1[c1]
            nums1[i] = n1
            c1 += 1
            i += 1


test_cases = [([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6])]


@pytest.mark.parametrize("nums1, m, nums2, n, expected", test_cases)
def test_merge_sorted_arrays(nums1, m, nums2, n, expected):
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    assert nums1 == expected
