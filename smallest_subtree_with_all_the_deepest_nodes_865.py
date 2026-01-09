from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        depth = {None:-1}
        def dfs(node, parent = None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        # print(max(depth, key=depth.get))
        max_depth = max(depth.values())

        def res(node):
            if not node or depth.get(node, None) == max_depth:
                return node
            l, r = res(node.left), res(node.right)
            return node if l and r else l or r
        
        return res(root)