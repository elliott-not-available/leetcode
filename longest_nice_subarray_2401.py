class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        # brute force, double loop, keep going untill not nice. return max length

        # optimised - > sliding window
        res = 0
        cur = 0
        cur_l = 0 
        l = 0
        
        for r in range(len(nums)):
            while (cur & nums[r]) == 1:
                cur = cur ^ nums[l] # XOR
                l += 1
                cur_l -= 1

            
            cur = cur | nums[r] # OR
            cur_l += 1
            
            res = max(res, cur_l)
                
        return res