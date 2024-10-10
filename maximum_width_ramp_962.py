# maximum_width_ramp_962
# https://leetcode.com/problems/maximum-width-ramp/description/?envType=daily-question&envId=2024-10-10

class Solution_BRUTE_FORCE:
    def maxWidthRamp(self, nums: list[int]) -> int:
        max_width = 0
        n = len(nums)

        # brute force
        for i in range(n):
            for j in range(n):
                if j <= i:
                    continue
                if nums[j] >= nums[i]:
                    max_width = max(max_width, j - i)

        return max_width


class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        n = len(nums)
        decreasing_stack = []

        for i in range(n):
            if not decreasing_stack or nums[decreasing_stack[-1]] > nums[i]:
                decreasing_stack.append(i)
        # print(decreasing_stack)
        max_width = 0

        for j in range(n-1, -1, -1):
            while decreasing_stack and nums[decreasing_stack[-1]] <= nums[j]:
                max_width = max(max_width, j - decreasing_stack.pop())

        return max_width
