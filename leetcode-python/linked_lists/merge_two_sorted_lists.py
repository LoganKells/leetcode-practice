import pytest
from typing import Optional
from util.linked_list import ListNode, build_linked_list, list_from_linked_list

# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def recurse(self, n1: ListNode, n2: ListNode):
        # Base case
        if n1 is None:
            return n2
        elif n2 is None:
            return n1

        if n1.val <= n2.val:
            n1.next = self.recurse(n1=n1.next, n2=n2)
            return n1
        else:
            n2.next = self.recurse(n1=n1, n2=n2.next)
            return n2

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        :param l1: sorted linked list
        :param l2: sorted linked list
        :return: Merge two sorted linked lists and return it as a sorted list.
        The list should be made by splicing together the nodes of the first two lists.
        """

        # Recursively append
        return self.recurse(n1=l1, n2=l2)


test_cases = [([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
              ([], [], []),
              ([], [0], [0])]


@pytest.mark.parametrize("l1, l2, expected", test_cases)
def test_merge_two_lists(l1, l2, expected):
    sol = Solution()

    # Build linked list
    l1_head = build_linked_list(nums=l1)
    l2_head = build_linked_list(nums=l2)

    # Merge two linked lists
    merged_head = sol.mergeTwoLists(l1=l1_head, l2=l2_head)

    # Test assertion
    merged_head_values = list_from_linked_list(head=merged_head)
    assert merged_head_values == expected