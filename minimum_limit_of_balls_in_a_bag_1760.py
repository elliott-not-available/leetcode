# minimum_limit_of_balls_in_a_bag_1760
# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/description/?envType=daily-question&envId=2024-12-07
from math import ceil

class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:

        def can_divide(max_balls: int):
            ops = 0
            for n in nums:
                ops += ceil(n / max_balls) - 1
                if ops > maxOperations:
                    return False
            return True
        
        l, r = 1, max(nums)

        while l < r:
            m = l+r // 2

            if can_divide(m):
                r = m
            else:
                l = m + 1

        return l