# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/?envType=daily-question&envId=2025-02-21

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# initial solution
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        # set root to 0?
        # left = 2*val + 1
        # right = 2*val + 2
        self.vals = set()
        root.val = 0
        self.vals.add(0)

        # node, direction, parent val
        st = []
        if root.left:
            st.append((root.left, 0, 0))
        if root.right:
            st.append((root.right, 1, 0)) 

        while st:
            node, dir, par = st.pop()

            if dir == 0:
                node.val = 2*par + 1
            if dir == 1:
                node.val = 2*par + 2
            self.vals.add(node.val)

            if node.left:
                st.append((node.left, 0, node.val))
            if node.right:
                st.append((node.right, 1, node.val))


    def find(self, target: int) -> bool:
        if target in self.vals:
            return True
        return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

# editorial
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.seen
    
    def dfs(self, current_node, current_val):
        if current_node is None:
            return
        self.seen.add(current_val)
        self.dfs(current_node.left, current_val*2 + 1)
        self.dfs(current_node.right, current_val*2 + 2)