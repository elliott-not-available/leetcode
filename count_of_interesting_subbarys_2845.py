# https://leetcode.com/problems/count-of-interesting-subarrays/description/?envType=daily-question&envId=2025-04-25
from collections import defaultdict
class Solution:
    def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
        N = len(nums)
        # count = [0] * N
        # cur_cnt = 0
        # for i in range(nums):
        #     if nums[i] % modulo == k:
        #         cur_cnt += 1

        #     count[i] = cur_cnt




        # return
        hm = defaultdict(int)
        res = 0
        cur = 0

        for i in range(N):

            if nums[i] % modulo == k:
                cur += 1
                cur = cur % modulo

            # dont understand this bit
            if cur == k:
                res += 1

            res += hm[(cur - k) % modulo]
            hm[cur] += 1
            
            # abc = (cur - k + modulo) % modulo
            # res += cnt[abc]
            # cnt[cur % modulo] += 1
        return res
        