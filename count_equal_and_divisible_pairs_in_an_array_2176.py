# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description/?envType=daily-question&envId=2025-04-17

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        # brute force o(n**2) - can be optimised
        N = len(nums)
        res = 0

        for i in range(N-1):
            for j in range(i+1, N):

                if (nums[i] == nums[j]) and (i*j % k == 0):
                    res += 1

        return res
        