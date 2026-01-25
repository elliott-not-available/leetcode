# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/?envType=daily-question&envId=2026-01-25

class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        
        if k == 1:
            return 0
        nums.sort()
        res = float('inf')
        # print(nums)
        for i in range(len(nums)-k+1):
            # cur_window = nums[i:i+k]
            # print(cur_window)
            # dif = cur_window[-1] - cur_window[0]
            res = min(res, nums[i+k-1] - nums[i])


        return res