from util.linked_list import build_linked_list, ListNode, list_from_linked_list
import pytest
from typing import List, Optional


# 24. Swap Nodes in Pairs
# see - https://leetcode.com/problems/swap-nodes-in-pairs/

class SolutionIterative:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create dummy head to start the cursor
        dummy_head = ListNode()
        dummy_head.next = head
        cursor = dummy_head

        while cursor is not None and cursor.next is not None and cursor.next.next is not None:
            # Values to swap
            first = cursor.next
            second = cursor.next.next

            # Swap first and second
            cursor.next = second
            first.next = second.next
            second.next = first

            # Select new cursor, with stride = 2
            cursor = first  # stride = 2 (due to first being swapped to second position at this point)

        # Return the final head after all swapping
        return dummy_head.next


class SolutionRecursive:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if head is None or head.next is None:
            return head

        # Swap first and second
        first = head
        second = head.next

        # Swap
        first.next = self.swapPairs(head=second.next)
        second.next = first

        # Cursor/head is the second node
        return second


test_cases = [([1, 2, 3, 4], [2, 1, 4, 3])]


@pytest.mark.parametrize("nums, expected", test_cases)
def test_swap_nodes_in_pairs_iterative(nums, expected):
    sol = SolutionIterative()
    head = build_linked_list(nums=nums)
    head_swapped = sol.swapPairs(head=head)
    head_swapped_nums = list_from_linked_list(head=head_swapped)
    assert head_swapped_nums == expected


@pytest.mark.parametrize("nums, expected", test_cases)
def test_swap_nodes_in_pairs_recursive(nums, expected):
    sol = SolutionRecursive()
    head = build_linked_list(nums=nums)
    head_swapped = sol.swapPairs(head=head)
    head_swapped_nums = list_from_linked_list(head=head_swapped)
    assert head_swapped_nums == expected
