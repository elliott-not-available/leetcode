# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description/?envType=daily-question&envId=2025-04-27

class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        # brute force O(n)
        N = len(nums)
        res = 0
        for i in range(N-2):
            a = nums[i] + nums[i+2]
            b = 0.5 * nums[i+1]
            res += 1 if a==b else 0
        
        return res