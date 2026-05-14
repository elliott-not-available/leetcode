# https://leetcode.com/problems/check-if-array-is-good/description/?envType=daily-question&envId=2026-05-14

class Solution:
    def isGood(self, nums: list[int]) -> bool:
        nums.sort()
        n = len(nums)

        for i in range(n-1):
            if nums[i] != i+1:
                return False
        return nums[n-1] == n-1
