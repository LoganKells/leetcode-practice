import pytest
from util.linked_list import build_linked_list, ListNode, list_from_linked_list


# 237. Delete Node in a Linked List
# see - https://leetcode.com/problems/delete-node-in-a-linked-list/

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # n = node.copy()
        node.val = node.next.val
        node.next = node.next.next


test_cases = [([4, 5, 1, 9], 5, [4, 1, 9]),
              ([4, 5, 1, 9], 1, [4, 5, 9]),
              ([-3, 5, -99], -3, [5, -99])]


@pytest.mark.parametrize("nums, x, expected", test_cases)
def test_delete_node(nums, x, expected):
    idx = nums.index(x)
    nums_linked = build_linked_list(nums=nums)

    head = nums_linked
    for i in range(idx):
        head = head.next

    sol = Solution()
    sol.deleteNode(node=head)
    nums_x_removed_list = list_from_linked_list(nums_linked)

    assert nums_x_removed_list == expected
