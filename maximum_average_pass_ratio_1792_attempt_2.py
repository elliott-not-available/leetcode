# https://leetcode.com/problems/maximum-average-pass-ratio/?envType=daily-question&envId=2025-09-01

from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        # whichever ration increases the most from +1 / +1

        # calculate and keep sorted? min heap

        def incc(p, t):
            return ((p + 1) / (t + 1)) - (p / t)
        
        heap = []
        for pas, tot in classes:
            inc = incc(pas, tot)
            heap.append((-inc, pas, tot))

        heapq.heapify(heap)

        # print("before operation")
        # for i in heap:
        #     print(i[0], i[1], i[2])

        for i in range(extraStudents):
            cur, pas, tot = heapq.heappop(heap)
            # print(f"adding to {cur} {pas} {tot}")
            new = (-incc(pas+1, tot+1), pas+1, tot+1)
            # print(f"pushing {new[0]}, {new[1]}, {new[2]}")
            heapq.heappush(heap, new)

        res = sum(p/t for _,p,t in heap) / len(classes)

        # for i in heap:
        #     print (i[1], i[2])
        return res