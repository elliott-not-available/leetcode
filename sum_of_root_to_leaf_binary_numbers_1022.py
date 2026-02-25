# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/?envType=daily-question&envId=2026-02-24
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def get(node, n=0):
            if not node: return

            n = 2*n + node.val
            if not node.left and not node.right:
                self.res+=n

            get(node.left, n)
            get(node.right, n)
            return
            
        get(root)
        return self.res