# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description/?envType=daily-question&envId=2025-06-28

class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        
       N = len(nums)
       vals = [[i, nums[i]] for i in range(N)]
       vals.sort(key=lambda x: -x[1])
       vals = sorted(vals[:k])
       res = [val for _, val in vals]
       return res


        