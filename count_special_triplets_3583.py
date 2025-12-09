# https://leetcode.com/problems/count-special-triplets/description/?envType=daily-question&envId=2025-12-09
from collections import defaultdict
class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        mod = 10**9 + 7

        cnt = defaultdict(int) # could use counter
        cnt_partial = defaultdict(int)

        for n in nums:
            cnt[n] += 1

        res = 0

        for n in nums:
            target = n*2

            l = cnt_partial[target]
            
            cnt_partial[n] += 1

            r = cnt[target] - cnt_partial[target]
            
            res = (res + l*r) % mod

        return res