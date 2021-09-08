from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(nums: List[int]) -> ListNode:
    value_head = nums.pop(0)
    head = ListNode(val=value_head)
    cursor = head
    while len(nums) > 0:
        value_node = nums.pop(0)
        cursor.next = ListNode(val=value_node)
        cursor = cursor.next
    return head
