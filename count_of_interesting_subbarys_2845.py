# https://leetcode.com/problems/count-of-interesting-subarrays/description/?envType=daily-question&envId=2025-04-25

class Solution:
    def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
        N = len(nums)
        for l in range(N):
            for r in range(l, N):
                cur = nums[l:r]

                # for i in range segment check nums[i] % mod == k, if so cnt +1
                # now check cnt % mod == k


        return
        