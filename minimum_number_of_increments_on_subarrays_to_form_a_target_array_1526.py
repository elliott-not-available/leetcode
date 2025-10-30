# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/description/?envType=daily-question&envId=2025-10-30

class Solution:
    def minNumberOperations(self, target: list[int]) -> int:

        ## go backwards from target?
        # find_first value that is cur_max, check for same value neighbours
        # perform negation on cur_max values, check rest of array
        # curmax --

        # hahhaha there is a really smooth solution

        res = target[0]
        n = len(target)
        for i in range(1, n):
            res += max(target[i] - target[i-1], 0)
        return res