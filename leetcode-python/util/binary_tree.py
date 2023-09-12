from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_level_order(tree_values: List[int]) -> Optional[TreeNode]:
    '''

    :param tree_values: tree node values in level order
    :return: root: root of the tree
    '''
    if len(tree_values) == 0:
        return None
    root_value = tree_values.pop(0)
    root = TreeNode(val=root_value)
    roots_level = [root]

    nodes_in_level = 2
    while len(roots_level) != 0 and len(tree_values) != 0:
        new_root = roots_level.pop(0)
        l_value = tree_values.pop(0)
        r_value = tree_values.pop(0)
        node_left = TreeNode(val=l_value) if l_value is not None else None
        node_right = TreeNode(val=r_value) if r_value is not None else None
        new_root.left = node_left
        new_root.right = node_right
        if node_left is not None:
            roots_level.append(node_left)
        if node_right is not None:
            roots_level.append(node_right)
    return root


def test_build():
    null = None
    # tree_key_level_order = [3, 9, 20, null, null, 15, 7]
    tree_key_level_order = [1, null,2,null,3]
    build_tree_level_order(tree_values=tree_key_level_order)
