# minimum_number_of_operations_sort_a_binary_tree_by_level_2471
# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/?envType=daily-question&envId=2024-12-23

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict, deque


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def count_swaps(nums):
            swaps = 0
            s_nums = sorted(nums)
            n_map = {n:i for i, n in enumerate(nums)}

            for i, n in enumerate(nums):
                e = s_nums[i]
                if n != e:
                    j = n_map[e]
                    
                    n_map[n] = j
                    n_map[e] = i

                    nums[j] = n
                    nums[i] = e

                    swaps += 1
            return swaps
        
        q = deque([root])
        res = 0

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res += count_swaps(level)

        return res