# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/?envType=daily-question&envId=2026-01-07
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        res = -float('inf')
        tot = 0

        def dfs(node):
            nonlocal res, tot
            if not node: return 0

            s = node.val + dfs(node.left) + dfs(node.right)
            res = max(res, (tot - s) * s)
            return s
        # sum total, then test each breakpoint
        tot = dfs(root)
        dfs(root)

        return res % MOD