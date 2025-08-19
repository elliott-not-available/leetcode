# https://leetcode.com/problems/number-of-zero-filled-subarrays/?envType=daily-question&envId=2025-08-19

class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        # # brute force 2pntr kinda 1n scan (except when lots of 0's)
        # res = 0
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] == 0: 
        #         res += 1

        #         j = i+1
        #         while j < n and nums[j] == 0:
                    
        #             res += 1
        #             j += 1

        # return res

        # actual 1n scan
        res = 0
        cur = 0

        for n in nums:
            if n == 0:
                cur += 1
                res += cur
            else:
                cur = 0

        return res
        