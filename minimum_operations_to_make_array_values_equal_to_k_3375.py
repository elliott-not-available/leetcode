# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/?envType=daily-question&envId=2025-04-09

# from collections import Counter

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:

        minv = min(nums)

        if k > minv:
            return -1
        
        ## both seem about the same speed

        # seen = set(nums)
        # n = len(seen)

        # if k == minv:
        #     if n == 1:
        #         return 0
        #     return n - 1
        
        # if k < minv:
        #     if n == 1:
        #         return 1
        #     return n

        seen = set()

        for n in nums:
            if n > k and n not in seen:
                seen.add(n)

        return len(seen)
        