# target_sum_494
# https://leetcode.com/problems/target-sum/description/?envType=daily-question&envId=2024-12-26

from collections import deque, defaultdict

class Solution_bruteforce:
    # og
    # brute force, O(2^n), timelimit exceeded
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        
        # score_mapping = defaultdict(int)
        
        N = len(nums)

        q = deque([(1, nums[-1]), (1, nums[-1]*-1)]) # number count, current score

        res = 0
        while q:
            cur_i, cur_sum = q.pop()

            if cur_i == N and cur_sum == target:
                res +=1
            elif cur_i < N:

                q.append((cur_i + 1, cur_sum - nums[-(cur_i+1)]))
                q.append((cur_i + 1, cur_sum + nums[-(cur_i+1)]))

        return res
    

class Solution_not_optimised:
    # neet
    # brute force with hash map
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        hm = {}

        def backtrack(i, cur_sum):
            if (i, cur_sum) in hm:
                return hm[(i, cur_sum)]
            
            if i == len(nums):
                return 1 if cur_sum == target else 0
            
            hm[(i, cur_sum)] = (
                backtrack(i+1, cur_sum + nums[i]) + 
                backtrack(i+1, cur_sum - nums[i])
            )
            return hm[(i, cur_sum)]

        return backtrack(0, 0)
    

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1 # (0 sum) -> 1 way

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                next_dp[cur_sum + nums[i]] += count
                next_dp[cur_sum - nums[i]] += count
            dp = next_dp

        return next_dp[target]