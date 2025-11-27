# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/?envType=daily-question&envId=2025-11-27
import sys

class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        pre_sum = 0
        max_sum = -sys.maxsize

        ## answering wrong question
        # tot_sum = sum(nums)

        # while n % k != 0:
        #     tot_sum -= nums[n-1]
        #     n -= 1

        # return tot_sum

        ## kadane's alg

        min_so_far = [sys.maxsize] * k
        min_so_far[(k-1) % k] = 0

        for i, v in enumerate(nums):
            pre_sum += v
            max_sum = max(max_sum, pre_sum - min_so_far[i%k])
            min_so_far[i % k] = min(min_so_far[i%k], pre_sum)
        return max_sum



        