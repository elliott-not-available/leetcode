# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/?envType=daily-question&envId=2025-03-19


class Solution:
    def minOperations(self, nums: list[int]) -> int:


        # one operation = flip 3 consecutive elements
        res = 0

        def flip_window(i):
            nums[i] = 0 if nums[i] else 1 
            nums[i+1] = 0 if nums[i+1] else 1 
            nums[i+2] = 0 if nums[i+2] else 1 

        def result():
            if not nums[-1] or not nums[-2]:
                return -1
            return res

        for i in range(len(nums)-2):
            if nums[i] == 0:
                res += 1
                flip_window(i)


        return result()