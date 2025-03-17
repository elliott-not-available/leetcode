# kth_largest_sum_in_a_binary_tree_2583
# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/?envType=daily-question&envId=2024-10-22

from typing import Optional
from collections import deque
import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        scores = {1: root.val}

        def binary_tree_level_sum(root: Optional[TreeNode], level: int, scores: dict[int,int]) -> int:
            cur_score = 0
            cur_score += root.left.val if root.left else 0
            cur_score += root.right.val if root.right else 0

            if cur_score == 0:
                return

            if level in scores:
                scores[level] += cur_score
            else:
                scores[level] = cur_score

            if root.left:
                binary_tree_level_sum(root.left, level + 1, scores)
            if root.right:
                binary_tree_level_sum(root.right, level + 1, scores)

            return scores

        result = list(sorted(binary_tree_level_sum(root, 2, scores).values()))
        print(scores)
        print(result)

        if len(result) < k:
            return -1
        else:
            return result[-k]
        

class Solution_neet:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        min_heap = []

        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            heapq.heappush(min_heap, level_sum)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return -1 if len(min_heap) < k else min_heap[0]