# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=daily-question&envId=2026-01-06
from typing import Optional
# from collections import defaultdict
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # level_sum = defaultdict(int)

        # def dfs(node, current_depth):
        #     level_sum[current_depth] += node.val

        #     if node.left:
        #         dfs(node.left, current_depth+1)

        #     if node.right:
        #         dfs(node.right, current_depth+1)

        # dfs(root, 0)

        # res = 0
        # cur_max = 0
        # cur_sum = 0

        # for level in level_sum.keys():

        #     s = level_sum[level]
        #     new_sum = cur_sum + s

        #     if new_sum > cur_max:
        #         res = level
        #         cur_max = new_sum

        #     cur_sum = new_sum

        
        # return res

        # bfs not dfs
        cur_level = 1
        maxi = float('-inf')
        res = 1
        q = deque([root])

        while q:
            cur_sum = 0
            level_size = len(q)

            for _ in range(level_size):
                node = q.popleft()
                cur_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if cur_sum > maxi:
                maxi = cur_sum
                res = cur_level
            cur_level += 1
        return res