import pytest
from typing import Optional, List
from util.binary_tree import TreeNode, build_tree_level_order


# 101. Symmetric Tree
# see - https://leetcode.com/problems/symmetric-tree/
VALUE_NO_NODE = -101

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True

        left_values = []
        right_values = []

        # Change the order of post order, based on left vs. right sides.
        # Left sub-tree traversal: left->right->root
        # Right sub-tree traversal: right->left->root
        if root.left is not None:
            left_values = [root.left.val]
            self.traverse_pre_order(root=root.left, values=left_values, order='left')
        if root.right is not None:
            right_values = [root.right.val]
            self.traverse_pre_order(root=root.right, values=right_values, order='right')

        # check if left and right values are equal
        if left_values == right_values:
            return True
        else:
            return False

    def traverse_pre_order(self, root: TreeNode, values: List[int], order: str) -> int:
        # Base case
        if root is None:
            return VALUE_NO_NODE

        # recursive, post order traversal
        if order == 'left':
            # Traverse Left nodes
            new_val = self.traverse_pre_order(root=root.left, values=values, order='left') if root.left else VALUE_NO_NODE
            values.append(new_val)

            # Traverse Right nodes
            new_val = self.traverse_pre_order(root=root.right, values=values, order='right') if root.right else VALUE_NO_NODE
            values.append(new_val)
        else:
            # Traverse Right nodes
            new_val = self.traverse_pre_order(root=root.right, values=values, order='right') if root.right else VALUE_NO_NODE
            values.append(new_val)

            # Traverse Left nodes
            new_val = self.traverse_pre_order(root=root.left, values=values, order='left') if root.left else VALUE_NO_NODE
            values.append(new_val)

        return root.val


null = None
test_cases = [
    ([1, 2, 2, null, 3, null, 3], False),
    ([1, 2, 2, 3, 4, 4, 3, 5, 4, 7, 9, 9, 7, 4, 5], True),
    ([1, 2, 2, 3, 4, 4, 3], True)
]


@pytest.mark.parametrize("nums, expected", test_cases)
def test_symmetric_bst(nums, expected):
    sol = Solution()
    tree_root = build_tree_level_order(tree_values=nums)
    symmetric_tree_flag = sol.isSymmetric(root=tree_root)
    assert symmetric_tree_flag == expected
