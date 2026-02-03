# https://leetcode.com/problems/trionic-array-i/description/?envType=daily-question&envId=2026-02-03

class Solution:
    def isTrionic(self, nums: list[int]) -> bool:

        if nums[0] >= nums[1]:
            return False
        
        n = len(nums)
        cnt = 1

        for i in range(2, n):

            if nums[i-1] == nums[i]:
                return False

            dif_1 = nums[i-2] - nums[i-1]
            dif_2 = nums[i-1] - nums[i]

            if dif_1 * dif_2 < 0:
                cnt += 1
        return cnt == 3
        