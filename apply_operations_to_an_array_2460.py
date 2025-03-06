# https://leetcode.com/problems/apply-operations-to-an-array/?envType=daily-question&envId=2025-03-01

class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        N = len(nums)
        res = [0] * N
        j = 0

        for i in range(N-1):

            if nums[i] != nums[i+1]:
                if nums[i] != 0:
                    res[j] = nums[i]
                    j += 1
            else:
                new = nums[i]*2
                if new != 0:
                    res[j] = new
                    j += 1
                nums[i+1] = 0

        if nums[-1] != 0:
            res[j] = nums[-1]

        return res


        