# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description/?envType=daily-question&envId=2025-04-28


class Solution:
    def countSubarrays(self, nums: list[int], k: int):
        # sliding windowish - 
        N = len(nums)
        cur, res = 0 , 0
        l = 0

        for r in range(N):
            cur += nums[r]

            while cur * (r - l + 1) >= k:
                cur -= nums[l]
                l += 1

            res += (r - l + 1)
        return res