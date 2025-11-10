# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/description/?envType=daily-question&envId=2025-11-10
# from collections import Counter

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        if sum(nums) == 0:
            return 0
        
        res = 0
        stack = []

        for n in nums:

            while stack and stack[-1] > n:
                stack.pop()
            
            if n == 0:
                continue

            if not stack or stack[-1] < n:
                res += 1
                stack.append(n)

        return res
        
