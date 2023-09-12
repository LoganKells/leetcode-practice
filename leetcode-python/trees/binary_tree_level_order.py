# See - https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        # Add root
        node_level = [root]
        # data.append([root.val])

        data_level = []
        data = []
        # Traverse each level and add to a list for the level
        while len(node_level) > 0:
            node_level_start_size = len(node_level)

            for i in range(node_level_start_size):
                node = node_level.pop(0)
                data_level.append(node.val)
                if node.left is not None:
                    node_level.append(node.left)
                if node.right is not None:
                    node_level.append(node.right)

            if len(data_level) > 0:
                data.append(data_level)
            data_level = []

        return data


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        # values to return in list
        data = [[root.val]]

        # que to pop off the left-most node
        queue_level = []

        # Process each node
        queue_level.append(root)
        data_level = []
        while len(queue_level) > 0:
            count_node = len(queue_level)  # Nodes in queue

            for i in range(count_node):
                node = queue_level.pop(0)  # Pop the left-most node (FIFO queue)
                if node.left is not None:
                    data_level.append(node.left.val)
                    queue_level.append(node.left)
                if node.right is not None:
                    data_level.append(node.right.val)
                    queue_level.append(node.right)
            if len(data_level) > 0:
                data.append(data_level)
            data_level = []

        return data