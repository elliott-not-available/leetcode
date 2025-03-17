# continuous_subarrays_2762
# https://leetcode.com/problems/continuous-subarrays/description/?envType=daily-question&envId=2024-12-14

class Solution_og:
    # brute force - time limit exceeded n**2 * n**2
    def continuousSubarrays(self, nums: list[int]) -> int:

        def rule(sub_arr: list[int]):
            # print(sub_arr)
            n = len(sub_arr)
            for i in range(n):
                for j in range(n):
                    out = abs(sub_arr[i] - sub_arr[j])
                    if out > 2:
                        return False
            return True
        
        res = 0

        for j in range(len(nums)):
            cur_l = j
            for i in range(len(nums) - cur_l):
                sub = nums[i:i+cur_l+1]

                if rule(sub):
                    res +=1


        return res
        
from collections import defaultdict

class Solution:
    # editorial sliding windoq
    def continuousSubarrays(self, nums: list[int]) -> int:
        res = 0
        N = len(nums)

        freq = defaultdict(int)
        l = r = 0

        while r < N:
            freq[nums[r]] += 1

            while (max(freq) - min(freq)) > 2:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1

            res += (r - l + 1)
            r += 1

        return res

import heapq

class Solution:
    # editorial double prio heapq
    def continuousSubarrays(self, nums: list[int]) -> int:
        min_heap = []
        max_heap = []
        l = r = 0
        res = 0

        while r < len(nums):
            heapq.heappush(min_heap, (nums[r], r))
            heapq.heappush(max_heap, (-1 * nums[r], r))

            while l < r and (-max_heap[0][0] - min_heap[0][0]) > 2:
                l +=1

                while min_heap and min_heap[0][1] < l:
                    heapq.heappop(min_heap)
                while max_heap and max_heap[0][1] < l:
                    heapq.heappop(max_heap)

            res += (r - l + 1)
            r += 1
        return res
