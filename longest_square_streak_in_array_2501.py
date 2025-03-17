# longest_square_streak_in_array_2501
# https://leetcode.com/problems/longest-square-streak-in-an-array/
from collections import defaultdict


class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        nums = set(sorted(nums))
        streaks = defaultdict(int)
        streaks[-1] = -1
        
        def check_streak(n, nums, cur_streak):

            if n*n in streaks:
                return streaks[n*n] + cur_streak
            if n*n in nums:
                return check_streak(n*n, nums, cur_streak+1)
            return cur_streak

        for n in nums:
            streaks[n] = check_streak(n, nums, 1)

        max_streak = max(streaks.values())

        if max_streak == 1:
            return -1
        return max_streak
        

        