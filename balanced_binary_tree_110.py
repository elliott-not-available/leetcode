# https://leetcode.com/problems/balanced-binary-tree/?envType=daily-question&envId=2026-02-08
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def height(node):
            # for left and right check depth is difference in depth is <= 1
            if not node:
                return 0

            l = height(node.left)
            if l == -1:
                return -1

            r = height(node.right)
            if r == -1:
                return -1

            if abs(l - r) > 1:
                return -1

            return max(l, r) + 1


        return height(root) != -1