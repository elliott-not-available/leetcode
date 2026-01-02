# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/?envType=daily-question&envId=2026-01-02
from collections import Counter
class Solution: 
    def repeatedNTimes(self, nums: list[int]) -> int:
        c = Counter(nums)
        n = len(nums)

        for k, v in c.items():
            if v == n/2:
                return k
        return False
        