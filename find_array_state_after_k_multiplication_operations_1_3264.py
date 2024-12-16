# find_array_state_after_k_multiplication_operations_1_3264
# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/?envType=daily-question&envId=2024-12-16
import heapq


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:

        hq = [(v, i) for i,v in enumerate(nums)]
        heapq.heapify(hq)

        for _ in range(k):
            v, i = heapq.heappop(hq)
            nums[i] *= multiplier
            heapq.heappush(hq, (nums[i], i))
            
        return nums

        