# height_of_binary_tree_after_subtree_removal_queries_2458
# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # not working
    def treeQueries(self, root: Optional[TreeNode], queries: list[int]) -> list[int]:
        # hashmap of value: height
        res_map = {}
        height = 0
        q = deque([(root, height)])

        def get_height_without(val: int) -> int:
            nonlocal root
            max_h = 0
            h = 0
            q = deque([(root, h)])
            while q:
                for _ in range(len(q)):
                    node, h = q.popleft()

                    if h > max_h:
                        max_h = h

                    if node.val == val:
                        continue 

                    if node.left:
                        if node.left.val != val:
                            q.append((node.left, h+1))

                    if node.right:
                        if node.right.val == val:
                            q.append((node.right, h+1))
            return max_h


        while q:
            for _ in range(len(q)):
                node, height = q.popleft()
                res_map[node.val] = get_height_without(node.val)
                if node.left:
                    q.append((node.left, height+1))
                if node.right:
                    q.append((node.right, height+1))


        print(res_map)
        return [res_map[q] for q in queries]