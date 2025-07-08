# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/?envType=daily-question&envId=2025-07-07
from heapq import heappush, heappop

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:

        events.sort()

        mh = []
        day, index, n, res = 0, 0, len(events), 0

        while mh or index < n:
            if not mh:
                day = events[index][0]

            # add all ends to heap that start before= day
            while index < n and events[index][0] <= day:
                heappush(mh, events[index][1])
                index += 1
            
            # pops earliest end
            heappop(mh)
            res += 1
            day += 1

            # pop all values where end is before day
            while mh and mh[0] < day:
                heappop(mh)

        return res