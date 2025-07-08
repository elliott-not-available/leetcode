# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/description/?envType=daily-question&envId=2025-07-08
from bisect import bisect_right
class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        # dfs tree - include / dont include
        n = len(events)
        events.sort()
        starts = [start for start, _, _ in events]
        dp = [[-1]*n for _ in range(k + 1)]

        def dfs(cur_ind, cnt):
            if cnt == 0 or cur_ind == n:
                return 0
            if dp[cnt][cur_ind] != -1:
                return dp[cnt][cur_ind]
            
            nxt_ind = bisect_right(starts, events[cur_ind][1])
            dp[cnt][cur_ind] = max(dfs(cur_ind+1, cnt), events[cur_ind][2] + dfs(nxt_ind, cnt-1))
            return dp[cnt][cur_ind]
        return dfs(0, k)
        