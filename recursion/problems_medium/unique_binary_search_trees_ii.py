from typing import List, Optional

# See - https://leetcode.com/problems/unique-binary-search-trees-ii/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # generate a queue of tree node values, any of which can be root of a tree

        def build_tree_recursive(start: int, end: int, tree_values: List[int]):
            if start > end:
                return [None, ]

            trees = []

            for i in range(start, end + 1):
                # i: new root
                left_values = list(range(start, i))
                left_trees = build_tree_recursive(start=start, end=i - 1, tree_values=left_values)
                right_values = list(range(i + 1, end))
                right_trees = build_tree_recursive(start=i + 1, end=end, tree_values=right_values)

                # Create trees with given root, and remaining values
                for left_value in left_trees:
                    for right_value in right_trees:
                        root = TreeNode(i)  # current sub-tree root
                        root.left = left_value
                        root.right = right_value
                        trees.append(root)
            return trees

        return build_tree_recursive(start=1, end=n, tree_values=list(range(1, n + 1)))


def test_generate_tree():
    n = 3
    solution = Solution()
    trees = solution.generateTrees(n=n)

    print(f"root: {trees}")
