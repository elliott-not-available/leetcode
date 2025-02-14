# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description/?envType=daily-question&envId=2025-02-13

import heapq

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        min_heap = nums
        heapq.heapify(min_heap)
        ops = 0

        while min_heap:
            first = heapq.heappop(min_heap)

            if first >= k:
                return ops

            second = heapq.heappop(min_heap)

            ins = min(first, second)*2 + max(first, second)

            heapq.heappush(min_heap, ins)

            ops += 1
        return ops
        

        