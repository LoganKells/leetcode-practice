from typing import List, Optional
from util.binary_tree import TreeNode

# 95. Unique Binary Search Trees II
# See - https://leetcode.com/problems/unique-binary-search-trees-ii/


class Solution:
    trees_all = []

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # Recursively build the left and right sub trees, given some root value
        trees = self.post_order_build(start=1, end=n)
        return trees

    def post_order_build(self, start: int, end: int):
        # Base case
        if start > end:
            return [None, ]

        sub_tree = []

        # Build subtrees based on new start value, i
        for i in range(start, end + 1):
            # Post-order traversal
            # left_tree_values = list(range(start, i))
            left_tree_values = self.post_order_build(start=start, end=i - 1)

            # right_tree_values = list(range(i + 1, end))
            right_tree_values = self.post_order_build(start=i + 1, end=end)

            z= 1
            # Add the values to the tree
            for value_l in left_tree_values:
                for value_r in right_tree_values:
                    root = TreeNode(val=i, left=value_l, right=value_r)
                    sub_tree.append(root)
        return sub_tree


def test_generate_tree():
    n = 3
    solution = Solution()
    trees = solution.generateTrees(n=n)

    print(f"root: {trees}")
