from typing import List
import pytest

# 189. Rotate Array
# See - https://leetcode.com/problems/rotate-array/

class SolutionSlow:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx_l = 0
        idx_r = len(nums) - 1
        count = 0
        while count < k:
            # Swap
            element_last = nums.pop()
            nums.insert(0, element_last)
            count += 1
        return nums


class SolutionFastReverse:
    def reverse(self, start: int, end: int, nums: List[int]) -> List[int]:
        """
        :param start: reverse start index
        :param end: reverse end index
        :param nums: list of integers
        :return:
        """
        while start < end:
            # Swap elements to reverse
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums

    def rotate(self, nums: List[int], k: int) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k > n:
            k = k % n
        # Reverse all elements
        nums = self.reverse(start=0, end=n - 1, nums=nums)

        # Reverse the first k elements
        nums = self.reverse(start=0, end=k - 1, nums=nums)

        # Reverse the last k elements
        nums = self.reverse(start=k, end=n - 1, nums=nums)

        return nums


test_cases = [([1, 2, 3], 4, [3, 1, 2]),
              ([-1], 2, [-1]),
              ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])]


@pytest.mark.parametrize("list_input, k, expected", test_cases)
def test_rotate_slow(list_input, k, expected):
    sol = SolutionSlow()
    list_rotated = sol.rotate(nums=list_input, k=k)

    assert list_rotated == expected


@pytest.mark.parametrize("list_input, k, expected", test_cases)
def test_rotate_fast(list_input, k, expected):
    sol = SolutionFastReverse()
    list_rotated = sol.rotate(nums=list_input, k=k)

    assert list_rotated == expected
