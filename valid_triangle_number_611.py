# https://leetcode.com/problems/valid-triangle-number/description/?envType=daily-question&envId=2025-09-26

class Solution:
    def triangleNumber(self, nums: list[int]) -> int:

        nums.sort()
        cnt = 0

        for i in range(len(nums)-1, -1, -1):
            l, r = 0, i-1

            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    cnt += r - l
                    r -= 1
                else:
                    l += 1
        return cnt
        