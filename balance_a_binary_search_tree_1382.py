# https://leetcode.com/problems/balance-a-binary-search-tree/description/?envType=daily-question&envId=2026-02-09
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: Optional[TreeNode]):# -> Optional[TreeNode]:
        # doesnt work because return isnt treenode??

        def store_nodes(node, node_values):

            if not node:
                return
            
            node_values.append(node.val)
            store_nodes(node.left, node_values)
            store_nodes(node.right, node_values)

        def create_bst(node_values, start, end):# -> Optional[TreeNode]:

            if start > end:
                return None
            
            mid = start + (end-start) // 2

            l = create_bst(node_values, start, mid-1)
            r = create_bst(node_values, mid+1, end)

            res = TreeNode(node_values[mid], l, r)

            return res

        node_values = []
        store_nodes(root, node_values)
        print(node_values)
        new_root = create_bst(node_values, 0, len(node_values)-1)
        print(new_root, new_root.val, new_root.left, new_root.right)
        return new_root