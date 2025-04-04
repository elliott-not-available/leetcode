# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/description/?envType=daily-question&envId=2025-04-03

class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        # did something similar yesterday

        # for each n in nums i want to find the value that optimises (nums[i]-nums[j])*nums[k]
        # where i > j > k

        # therefor assuming k as the single traversal, i want to maximise nums[i] - nums[j]
        # max(nums[:i+1]) , min(nums[i+1:k])
        
        res = 0
        l = nums[0]
        max_diff = 0
        N = len(nums)

        for k in range(1, N):

            cur = max_diff * nums[k]
            res = max(res, cur)
            
            l = max(l, nums[k])
            max_diff = max(max_diff, l - nums[k])

        return res
        