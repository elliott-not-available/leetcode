# maximum_sum_of_distinct_subarrays_with_length_k_2461
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/?envType=daily-question&envId=2024-11-19

class Solution_og:
    # timelimit exceeded o(n*k) (bruteforce)
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:

        w_max = 0
        i = 0
        while i+k <= len(nums):
            window = nums[i:i+k]

            if len(set(window)) == k:
                w_sum = sum(window)

                if w_sum > w_max: 
                    w_max = w_sum

            i+=1
            
        return w_max
    

from collections import defaultdict

class Solution:
    # neeted - optimised sliding window
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        count = defaultdict(int)
        cur_sum = 0

        l = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            count[nums[r]] += 1

            if r-l+1 > k :
                count[nums[l]] -= 1

                if count[nums[l]] == 0:
                    count.pop(nums[l])

                cur_sum -= nums[l]
                l += 1

            if len(count) == r - l + 1 == k:
                res = max(cur_sum, res)
            
        return res
        

class Solution:
    # neeted - optimised sliding window
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        prev_idx = {}
        cur_sum = 0

        l = 0
        for r in range(len(nums)):
            cur_sum += nums[r]

            i = prev_idx.get(nums[r], -1)

            while l <= i or r-l+1 > k:
                cur_sum -= nums[l]
                l += 1


            if r - l + 1 == k:
                res = max(cur_sum, res)

            prev_idx[nums[r]] = r
            
        return res