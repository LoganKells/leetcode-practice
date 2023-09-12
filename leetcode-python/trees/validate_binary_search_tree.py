from typing import Optional
import pytest
import math
from util.binary_tree import build_tree_level_order, TreeNode

# 98. Validate Binary Search Tree
# see - https://leetcode.com/problems/validate-binary-search-tree/

class Solution:
    valid = True

    def post_order(self, node: TreeNode, val_max: int, val_min: int) -> None:
        if node is None or node.val is None:
            return None

        if node.val <= val_min or node.val >= val_max:
            self.valid = False

        if node.left is not None:
            self.post_order(node=node.left, val_max=node.val, val_min=val_min)
        if node.right is not None:
            self.post_order(node=node.right, val_max=val_max, val_min=node.val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # depth first search
        # post order traversal
        self.post_order(node=root, val_max=math.inf, val_min=-1 * math.inf)
        return self.valid


null = None
test_cases = [([5, 4, 6, null, null, 3, 7], False),
              ([2, 1, 3], True)]


@pytest.mark.parametrize("tree_list, expected", test_cases)
def test_validate_bst(tree_list, expected):
    # create binary search tree (bst)
    bst = build_tree_level_order(tree_values=tree_list)

    # Test if bst is valid
    sol = Solution()
    valid_bst = sol.isValidBST(root=bst)

    assert valid_bst == expected
