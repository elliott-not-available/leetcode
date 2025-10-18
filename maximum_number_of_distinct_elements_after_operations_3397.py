# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/description/?envType=daily-question&envId=2025-10-18
import math

class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        nums.sort()
        res = 0
        prev = -1* math.inf

        for n in nums:
            nxt = max(n-k, prev+1)
            cur = min(nxt, n+k)

            if cur > prev:
                res += 1
                prev = cur

        return res
        