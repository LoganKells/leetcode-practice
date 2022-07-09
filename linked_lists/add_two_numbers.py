import pytest
from typing import Optional
from util.linked_list import ListNode, build_linked_list, list_from_linked_list


# 2. Add Two Numbers
# see https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Traverse each list, add numbers
        nums_l1, nums_l2 = [], []
        while l1:
            nums_l1.append(l1.val)
            l1 = l1.next
        while l2:
            nums_l2.append(l2.val)
            l2 = l2.next

        # Build numbers from arrays in reverse [2, 4, 3] = 342
        power_l1, power_l2 = len(nums_l1) - 1, len(nums_l2) - 1
        total_l1, total_l2 = 0, 0
        # Debug:
        # print(f"nums_l1: {nums_l1}")
        # i_s = list(range(len(nums_l1)))[::-1]
        # print(f"i values: {i_s}")
        for i in list(range(len(nums_l1)))[::-1]:
            total_l1 += (10 ** power_l1) * nums_l1[i]
            power_l1 -= 1
        for i in list(range(len(nums_l2)))[::-1]:
            total_l2 += (10 ** power_l2) * nums_l2[i]
            power_l2 -= 1
        total = total_l1 + total_l2

        # Debug:
        # print(total)

        if total == 0:
            # Edge case
            return ListNode(val=0, next=None)
        else:
            # Build a list of the numbers comprising the total: 807 -> [8, 0, 7]
            total_nums = []
            while total > 0:
                remainder = total % 10
                total_nums.append(remainder)

                # Update total
                total -= remainder
                total = total // 10

            # Build nodes from linked list
            head = ListNode(val=total_nums.pop(0), next=None)
            dummy_head = ListNode(val=0, next=head)
            while len(total_nums) > 0:
                head.next = ListNode(val=total_nums.pop(0), next=None)
                head = head.next

            return dummy_head.next


test_cases = [([2, 4, 3], [5, 6, 4], [7, 0, 8]),
              ([0], [0], [0]),
              ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
              ([0, 0, 1], [0, 0, 1], [0, 0, 2])]


@pytest.mark.parametrize("l1, l2, expected", test_cases)
def test_add_two_numbers(l1, l2, expected):
    sol = Solution()
    l1_head, l2_head = build_linked_list(nums=l1), build_linked_list(nums=l2)
    total_head = sol.addTwoNumbers(l1=l1_head, l2=l2_head)
    total_list = list_from_linked_list(head=total_head)
    assert total_list == expected
