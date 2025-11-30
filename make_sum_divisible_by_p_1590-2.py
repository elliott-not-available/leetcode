# https://leetcode.com/problems/make-sum-divisible-by-p/?envType=daily-question&envId=2025-11-30
# from collections import defaultdict
class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        ## didnt work (also didnt do index n-1 properly)
        # tot = sum(nums)
        # if tot%p==0:
        #     return 0
        # if p > tot:
        #     return -1
        
        # n = len(nums)
        # sub_arrays_sums = {} # i = ss sum, sas[i] = min size

        # for i in range(n-1):
        #     for j in range(i+1, n+1):
        #         print(i, j, nums[i:j])
        #         cur_len = j-i
        #         cur_sum = sum(nums[i:j])

        #         if cur_sum in sub_arrays_sums:
        #             sub_arrays_sums[cur_sum] = min(cur_len, sub_arrays_sums[cur_sum])
        #         else:
        #             sub_arrays_sums[cur_sum] = cur_len


        # if tot%p in sub_arrays_sums:
        #     return sub_arrays_sums[tot%p]
        # else:
        #     return -1

        n = len(nums)
        tot = sum(nums)
        tar = tot%p

        if tar ==0:
            return 0
        if p > tot:
            return -1
        
        res_map = {0: -1}
        cur_sum = 0
        min_len = n

        for i in range(n):
            cur_sum = (cur_sum + nums[i]) % p
            aim = (cur_sum - tar + p) % p

            if aim in res_map:
                min_len = min(min_len, i-res_map[aim])

            res_map[cur_sum] = i

        return -1 if min_len == n else min_len