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
        l = TreeNode(val=tree_values.pop(0))
        r = TreeNode(val=tree_values.pop(0))
        new_root.left = l
        new_root.right = r
        if l.val is not None:
            roots_level.append(l)
        if r.val is not None:
            roots_level.append(r)
    return root


def test_build():
    null = None
    # tree_key_level_order = [3, 9, 20, null, null, 15, 7]
    tree_key_level_order = [1, null,2,null,3]
    build_tree_level_order(tree_values=tree_key_level_order)
