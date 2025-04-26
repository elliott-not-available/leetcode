# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/?envType=daily-question&envId=2025-04-26
# from collections import deque

class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        # # brute force o(n**2) - timelimit exceeded
        # N = len(nums)
        # res = 0
        # for i in range(N):
        #     cur_min = nums[i]
        #     cur_max = nums[i]

        #     for j in range(i, N):
        #         # print(f"ind: {i}, {j}")

        #         if nums[j] > cur_max:
        #             cur_max = nums[j]
        #         if nums[j] < cur_min:
        #             cur_min = nums[j]

        #         # print(f"min: {cur_min}, {minK}")
        #         # print(f"max: {cur_max}, {maxK}")

        #         if cur_min < minK:
        #             continue
        #         if cur_max > maxK:
        #             continue

        #         if cur_max == maxK and cur_min == minK:
        #             res += 1

        # return res
        ##################################################
        # # Double deque - not entirely understood - works but only just
        # res = 0
        # l = 0
        # dq_min = deque()
        # dq_max = deque()

        # for i in range(len(nums)):

        #     if nums[i] < minK or nums[i] > maxK:
        #         # nums[i] not in range, go next
        #         dq_min.clear()
        #         dq_max.clear()
        #         l = i + 1
        #         continue
            
        #     # increasing (only add if larger, otherwise pop untill true)
        #     while dq_min and nums[dq_min[-1]] >= nums[i]:
        #         dq_min.pop()
        #     dq_min.append(i)

        #     # decreasing (only add if smaller, otherwise pop untill true)
        #     while dq_max and nums[dq_max[-1]] <= nums[i]:
        #         dq_max.pop()
        #     dq_max.append(i)

        #     if nums[dq_min[0]] == minK and nums[dq_max[0]] == maxK:
        #         start = min(dq_min[0], dq_max[0])
        #         res += (start - l + 1)
            
        # return res
        ##################################################
        # kidna sliding window
        res = 0
        start = -1
        mini = -1
        maxi = -1

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                start = i
                continue

            if nums[i] == maxK:
                maxi = i
            if nums[i] == minK:
                mini = i

            if maxi > start and mini > start:
                valid = min(mini, maxi) - start
                res += valid
        return res

