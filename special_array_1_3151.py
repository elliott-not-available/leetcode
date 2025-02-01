# https://leetcode.com/problems/special-array-i/description/?envType=daily-question&envId=2025-02-01

class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:

        # could be a tiny bit more efficient to create mod array first
        # and then loop through that array

        for i in range(len(nums)-1):
            if nums[i] % 2 == nums[i+1] % 2:
                return False
        return True