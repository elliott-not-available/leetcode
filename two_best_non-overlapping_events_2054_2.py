# https://leetcode.com/problems/two-best-non-overlapping-events/?envType=daily-question&envId=2025-12-23
from collections import deque

class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        end_sorted = deque(sorted(events, key=lambda x: x[1]))
        start_sorted = sorted(events, key=lambda x:x[0])

        # n = len(events)
        res = max(v for _, _, v in events)
        end_max = 0

        for s, _, s_v in start_sorted:
            while end_sorted and end_sorted[0][1] < s:
                _, _, end_v = end_sorted.popleft()
                end_max = max(end_max, end_v)
            res = max(res, s_v + end_max)

        return res