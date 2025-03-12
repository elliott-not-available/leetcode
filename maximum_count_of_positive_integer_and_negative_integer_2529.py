# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/?envType=daily-question&envId=2025-03-12

class Solution:
    def maximumCount(self, nums: list[int]) -> int:

        neg = 0
        zeros = 0
        N = len(nums)

        for i in range(N):
            if nums[i] < 0:
                neg += 1
            elif nums[i] == 0:
                zeros += 1
                continue
            else:
                return max(neg, N - neg - zeros)
        return max(neg, N - neg - zeros)
        