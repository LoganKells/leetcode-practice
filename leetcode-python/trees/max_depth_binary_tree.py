import pytest
from typing import Optional

from util.binary_tree import TreeNode, build_tree_level_order


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # we could store the depth of each node as we traverse it,
        # could do depth first search, post order
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1


null = None
test_cases = [([3, 9, 20, null, null, 15, 7], 3),
              ([1, None, 2], 2),
              ([], 0),
              ([0], 1)]


@pytest.mark.parametrize("nums, expected", test_cases)
def test_max_depth_bst(nums, expected):
    sol = Solution()
    root_bst = build_tree_level_order(tree_values=nums)
    depth = sol.maxDepth(root=root_bst)
    assert depth == expected
