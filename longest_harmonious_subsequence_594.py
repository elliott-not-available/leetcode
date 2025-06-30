# https://leetcode.com/problems/longest-harmonious-subsequence/?envType=daily-question&envId=2025-06-30

from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:

        cnt = Counter(nums)

        c_max = 0

        for k, v in cnt.items():

            nxt = cnt[k+1]
            if nxt:
                c_max = max(c_max, v + nxt)


        return c_max