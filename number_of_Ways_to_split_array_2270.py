# https://leetcode.com/problems/number-of-ways-to-split-array/description/?envType=daily-question&envId=2025-01-03

class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        l_sum = 0
        r_sum = sum(nums)
        valid_splits = 0

        def is_valid(l, r):
            if l >= r:
                return True
            return False
        
        for i in range(len(nums)-1):
            l_sum += nums[i]
            r_sum -= nums[i]

            if is_valid(l_sum, r_sum):
                valid_splits += 1

        return valid_splits
         