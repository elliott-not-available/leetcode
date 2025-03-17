# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/?envType=daily-question&envId=2025-01-25

from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        groups = [] # list of queues
        num_to_group = {} # nums[i] -> groups index

        for n in sorted(nums):
            if not groups or abs(n - groups[-1][-1]) > limit:
                groups.append(deque())
            groups[-1].append(n)
            num_to_group[n] = len(groups) - 1

        res = []
        for n in nums:
            j = num_to_group[n]
            res.append(groups[j].popleft())
        return res