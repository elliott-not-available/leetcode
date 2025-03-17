# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/?envType=daily-question&envId=2025-02-26

class Solution_bruteforce:
    # brute force
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        N = len(nums)
        max_v = 0
        for i in range(N):
            for j in range(i+1, N+1):
                subarray = nums[i:j]
                cur_sum = abs(sum(subarray))

                max_v = max(max_v, cur_sum)
        return max_v
    
class Solution:
    # pretty neeted, didnt really do anything myself
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        cur_sum = 0
        pre_max = 0
        pre_min = 0
        res = 0

        for n in nums:
            cur_sum += n

            res = max(res, abs(cur_sum - pre_min), abs(cur_sum - pre_max))
            pre_max = max(pre_max, cur_sum)
            pre_min = min(pre_min, cur_sum)

        return res