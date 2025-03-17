# find_largest_value_in_each_row_515
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/?envType=daily-question&envId=2024-12-25


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, defaultdict

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:

        largest = defaultdict(lambda:-1*float("inf"))
        q = deque([(root, 0)])

        while q:
            
            node, level = q.pop()
            if node:
                largest[level] = max(node.val, largest[level])

                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))

        return [largest[k] for k in largest.keys()]


