# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/?envType=daily-question&envId=2025-04-29

from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        # # brute force - barely passes timelimit - O(n) ish? its like 2n i think
        # N = len(nums)
        # m = max(nums)

        # cur = defaultdict(int)
        # cur[nums[0]] = 1

        # res = 0
        # r = 0

        # for l in range(N):
        #     if l != 0:
        #         cur[nums[l-1]] -= 1
                

        #     while (cur[m] < k) and (r < N-1):
        #         r += 1
        #         cur[nums[r]] += 1

        #     if cur[m] >= k:
        #         # print(N, l, r)
        #         # print(cur)
        #         res += N - r

        # return res
        ################################################
        # editorial solution - sliding the other way
        # same complexity, but doesnt use a map (so better)
        N = len(nums)
        m = max(nums)
        l = 0
        res = 0
        cur = 0

        for r in range(N):
            if nums[r] == m:
                cur += 1

            while cur == k:
                if nums[l] == m:
                    cur -= 1
                l += 1
            res += l

        return res