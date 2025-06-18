# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/?envType=daily-question&envId=2025-06-18

class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        res = []

        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] > k:
                return []
            res.append([nums[i], nums[i+1], nums[i+2]])

        return res