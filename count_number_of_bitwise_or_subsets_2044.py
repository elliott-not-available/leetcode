# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/?envType=daily-question&envId=2025-07-28
from typing import List

class Solution:
    def countMaxOrSubsets(self, nums):
        # TOP SOL
        maxOR = 0
        for num in nums:
            maxOR |= num

        def backtrack(index, currentOR):
            if index == len(nums):
                return 1 if currentOR == maxOR else 0

            if currentOR == maxOR:
                return 1 << (len(nums) - index)

            return backtrack(index + 1, currentOR | nums[index]) + \
                   backtrack(index + 1, currentOR)

        return backtrack(0, 0)
