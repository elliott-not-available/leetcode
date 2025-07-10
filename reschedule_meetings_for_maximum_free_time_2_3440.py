# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/?envType=daily-question&envId=2025-07-10


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:
        # greedy
        n = len(startTime)

        # n == 0?

        gaps = [0] * (n+1)
        gaps[0] = startTime[0]
        
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i-1]
        gaps[n] = eventTime - endTime[n-1]

        largest_right = [0] *(n+1)
        for i in reversed(range(n)):
            largest_right[i] = max(largest_right[i+1], gaps[i+1])
            
        max_free = 0
        largest_left = 0

        for i in range(1,n+1):
            dur = endTime[i-1] - startTime[i-1]
            can_fit_l = largest_left >= dur
            can_fit_r = largest_right[i] >= dur

            if can_fit_l or can_fit_r:
                merged = gaps[i-1] + gaps[i] + dur
                max_free = max(max_free, merged)
            
            max_free = max(max_free, gaps[i-1] + gaps[i])
            largest_left = max(largest_left, gaps[i-1])
            
        return max_free
        