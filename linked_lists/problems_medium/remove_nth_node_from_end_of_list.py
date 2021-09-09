import pytest
from typing import Optional
from util.linked_list import ListNode, build_linked_list, list_from_linked_list

# 19. Remove Nth Node From End of List
# see - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create dummy node to point to the real head
        dummy_node = ListNode()
        dummy_node.next = head

        # Get the actual idx of the node to remove, from the head
        list_length = 1
        node = head
        while node.next:
            list_length += 1
            node = node.next
        idx = list_length - n

        if list_length > 1:
            if idx == list_length - 1:
                for i in range(idx - 1):
                    head = head.next
                head.next = None
                return dummy_node.next
            for i in range(idx):
                head = head.next
            else:
                head.val = head.next.val if head.next is not None else head.val
                head.next = head.next.next if head.next is not None else None
            return dummy_node.next
        elif list_length == 1:
            head.val = None
            return None


test_cases = [([1,2,3], 1, [1, 2]),
    ([1, 2], 2, [2]),
    ([1, 2], 1, [1]),
    ([1], 1, [None]),
    ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5])

              ]


@pytest.mark.parametrize("nums, n, expected", test_cases)
def test_remove_node(nums, n, expected):
    # Create linked list from nums
    head = build_linked_list(nums=nums)

    # Run function to remove node at index n from end
    sol = Solution()
    sol.removeNthFromEnd(head=head, n=n)

    # Test result
    nums_node_removed = list_from_linked_list(head=head)
    assert nums_node_removed == expected
