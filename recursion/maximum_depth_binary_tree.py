from typing import Optional
import pytest
from util.binary_tree import TreeNode, build_tree_level_order


# see - https://leetcode.com/problems/maximum-depth-of-binary-tree/


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #         # Solution from Leetcode premium solution
        #         if root is None:
        #             return 0

        #         # Create a queue to pop off nodes from the left (FIFO queue method)
        #         q_level = [(1, root)]

        #         # Cursor move to each node in the que
        #         depth = 0
        #         while len(q_level) > 0:
        #             curr_depth, node = q_level.pop(0)  # pop left node from the queue (FIFO method)

        #             if node is not None:
        #                 depth = max(curr_depth, depth)
        #                 q_level.append((curr_depth + 1, node.left))
        #                 q_level.append((curr_depth + 1, node.right))

        #         return depth
        # My own method, similar to https://leetcode.com/problems/binary-tree-level-order-traversal/
        if root is None:
            return 0
        # Create a queue to pop off nodes from the left (FIFO queue method)
        q_level = [root]

        # Cursor move to each node in the que
        data = 1
        while len(q_level) > 0:
            count_node = len(q_level)
            count_node_level = 0
            for i in range(count_node):
                node = q_level.pop(0)  # pop left node from the queue (FIFO method)

                if node.left is not None:
                    q_level.append(node.left)
                    count_node_level += 1

                if node.right is not None:
                    q_level.append(node.right)
                    count_node_level += 1

            if count_node_level > 0:
                data += 1

        return data


null = None
test_cases = [([3, 9, 20, null, null, 15, 7], 3),
              ([1, null, 2], 2),
              ([], 0)]


@pytest.mark.parametrize("tree_values, depth", test_cases)
def test_iterative(tree_values, depth):
    root = build_tree_level_order(tree_values=tree_values)
    solution = Solution()
    max_tree_depth = solution.maxDepth(root=root)
    assert max_tree_depth == depth
