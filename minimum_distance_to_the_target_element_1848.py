# https://leetcode.com/problems/minimum-distance-to-the-target-element/?envType=daily-question&envId=2026-04-13

class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:

        n = len(nums)
        mmin = n+1
        res = -1

        for i in range(n):
            if nums[i] == target:
                if abs(i - start) <= mmin:
                    mmin = abs(i - start)


        return mmin