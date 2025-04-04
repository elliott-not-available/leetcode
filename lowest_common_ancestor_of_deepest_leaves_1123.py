# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # traverse tree once, updating res every time we go to a node with children

        # # missunderstood the question a bit
        # def dfsish(node, depth):

        #     res1, res2, res3 = (0, root), (0, root), (0, root)
            
        #     if node.left and node.right:# and depth >= max_depth:
        #         res1 = (depth, node)

        #     if node.left:
        #         res2 = dfsish(node.left, depth+1)
        #     if node.right:
        #         res3 = dfsish(node.right, depth+1)

        #     return max(res1, res2, res3)
            
        # r = dfsish(root, 0)
        # return r[1]

        def dfs(node, depth):
            if not node:
                return (depth + 1, None)
            
            l_d, l_n = dfs(node.left, depth + 1)
            r_d, r_n = dfs(node.right, depth + 1)

            # lhs deeper
            if l_d > r_d:
                return l_d, l_n
            # rhs deeper
            elif l_d < r_d:
                return r_d, r_n
            # both equal
            return l_d, node
                    
        _, res = dfs(root, 0)

        return res