# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/description/?envType=daily-question&envId=2025-04-08

from collections import defaultdict

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:

        # # kinda 2pntr brute force think its o(n)
        # N = len(nums)
        # i, j = 0, 0
        # ops = 0
        # # cntr = [0] * 10
        # cntr = defaultdict(int)

        # while i < N and j < N:

        #     cntr[nums[i]] += 1

        #     while cntr[nums[i]] > 1:

        #         cntr[nums[j]] -= 1
        #         if j+1 < N:
        #             cntr[nums[j+1]] -= 1
        #         if j+2 < N:
        #             cntr[nums[j+2]] -= 1

        #         j = j+3
        #         ops += 1
            
        #     i += 1
        # return ops
        #########################################################

        # go from back to front, checking for first duplicate
        # working out needed operations from there

        # still o(n) but should realistically be faster as it
        # stops at the first occurance of duplication instead of
        # scanning entire array

        seen = set()

        for i in reversed(range(len(nums))):
            if nums[i] in seen:
                return i//3 +1
            seen.add(nums[i])
        return 0
        