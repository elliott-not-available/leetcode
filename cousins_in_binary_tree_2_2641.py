# cousins_in_binary_tree_2_2641
# https://leetcode.com/problems/cousins-in-binary-tree-ii/description/?envType=daily-question&envId=2024-10-23

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # level sum
        # value = level sum - own.val - sibiling.val

        scores = {1: root.val}
        def level_sum(root: Optional[TreeNode], level: int, scores: dict[int,int]) -> int:
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
                level_sum(root.left, level + 1, scores)
            if root.right:
                level_sum(root.right, level + 1, scores)

            return scores
        
        level_sum(root, 2, scores)
        print(scores)

        def replace(root: Optional[TreeNode], level: int, scores: dict[int,int]) -> int:
            old_right = root.right.val if root.right else 0
            old_left = root.left.val if root.left else 0

            siblings = old_right + old_left

            if root.left:
                root.left.val = scores[level] - siblings
                replace(root.left, level + 1, scores)
            if root.right:
                root.right.val = scores[level] - siblings
                replace(root.right, level + 1, scores)

        root.val = 0
        replace(root, 2, scores)


        return root

from collections import deque
import heapq

class Solution_neet:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sum = []
        q = deque([root])

        while q:
            cur_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                cur_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level_sum.append(cur_sum)

        q = deque([(root, root.val)]) # node, child_sum
        level = 0
        while q:
            for i in range(len(q)):
                node, val = q.popleft()
                node.val = level_sum[level] - val

                child_sum = 0
                if node.left:
                    child_sum += node.left.val
                if node.right:
                    child_sum += node.right.val

                if node.left:
                    q.append((node.left, child_sum))
                if node.right:
                    q.append((node.right, child_sum))
            level += 1

        return root