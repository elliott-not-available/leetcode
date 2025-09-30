# https://leetcode.com/problems/find-triangular-sum-of-an-array/?envType=daily-question&envId=2025-09-30

class Solution:
    def triangularSum(self, nums: list[int]) -> int:

        def rec(inp):
            n = len(inp)
            if n == 2:
                return (inp[0] + inp[1]) % 10

            if n == 1:
                return inp[0]
            
            new_nums = []
            for i in range(n-1):
                new_nums.append((inp[i] + inp[i+1]) % 10)

            return rec(new_nums)

        return rec(nums)