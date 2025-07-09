# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/description/?envType=daily-question&envId=2025-07-09

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:

        n = len(startTime)
        res = 0

        tot = [0] * (n+1)

        for i in range(n):
            tot[i+1] = tot[i] + endTime[i] - startTime[i]

        for i in range(k-1, n):
            right = eventTime if i == n-1 else startTime[i+1]
            left = 0 if i == k-1 else endTime[i-k]
            res = max(res, right - left - (tot[i+1] - tot[i-k+1]))

        return res
        