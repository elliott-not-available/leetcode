# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/description/?envType=daily-question&envId=2026-03-13
import heapq
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        
        min_heap = []

        for i in range(len(workerTimes)):
            heapq.heappush(min_heap, (workerTimes[i], i, 1))

        res = 0
        mh = mountainHeight

        while mh > 0:
            t, index, x = heapq.heappop(min_heap)

            res = t
            mh-=1

            if mh>0:
                nx = x+1
                nt = workerTimes[index] * (nx * (nx+1) // 2)
                heapq.heappush(mh, (nt, index, nx))
        return res