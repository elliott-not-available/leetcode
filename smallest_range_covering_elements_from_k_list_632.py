# smallest_range_covering_elements_from_k_list_632
# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/?envType=daily-question&envId=2024-10-13

# TODO go through this solution and understand it
import heapq

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        # heapq iteration problem
        heap = []
        cur_max = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            cur_max = max(cur_max, nums[i][0])

        small = [float('-inf'), float('-inf')]

        while heap:
            cur_min, list_idx, i = heapq.headpop(heap)
            if (cur_max - cur_min < small[1] - small[0]) or ((cur_max - cur_min == small[1] - small[0]) and cur_min < small[0]):
                small = [cur_min, cur_max]
            if i + 1 < len(nums[list_idx]):
                nxt = nums[list_idx][i + 1]
                heapq.heappush(heap, (nxt, list_idx, i+1))
                cur_max = max(cur_max, nxt)
            else:
                break
        return small