# https://leetcode.com/problems/zero-array-transformation-iii/description/?envType=daily-question&envId=2025-05-22
# from collections import defaultdict
import heapq

class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        # not the correct solution
        # # sort q by length
        # # skip if overlap?

        # queries.sort(key=lambda t: t[1] - t[0])
        # print(queries[::-1])

        # # noverlap = []
        # res = 0
        # mini = queries[-1][0]
        # maxi = queries[-1][1]
        # # cur = defaultdict(int)
        # prefix = [0]*len(nums)

        # for start, end in queries[::-1]:

        #     # if (start not in cur) or (end not in cur):
        #     #     noverlap.append([start, end])

        #     #     for i in range(start, end):
        #     #         if i not in cur:
        #     #             cur[i] += 1
        #     if start >= mini and end <= maxi and sum(nums[start:end+1]) == 0:
        #         print(start, end, mini, maxi)
        #         res += 1
        #         continue

        #     mini = min(mini, start)
        #     maxi = max(maxi, end)

        #     prefix[start] -= 1
        #     prefix[end+1] += 1
        #     # noverlap.append([start, end])

        # return res
        ##############################################################
        # Use heap + sort

        queries.sort(key=lambda x: x[0])
        available = [] # max heap
        assigned = [] # min heap?
        cnt = 0
        k = 0

        for i in range(len(nums)):

            # while assinged is none empty and assigned[0] is less than i
            # pop assigned[0]
            while assigned and assigned[0] < i:
                heapq.heappop(assigned)

            # while k < len(queries) and queries[k][0] is less than or equal to i
            # push query[k] end to available max heap
            while k < len(queries) and queries[k][0] <= i:
                heapq.heappush(available, -queries[k][1])
                k += 1

            # while number of items in assigned is less than nums[i] and available (max) root is >= i
            # pop max available to (min heap) assigned
            # increment cnt
            
            while len(assigned) < nums[i] and available and -available[0] >= i:
                heapq.heappush(assigned, -heapq.heappop(available))
                cnt += 1

            if len(assigned) < nums[i]:
                return -1
            
        return len(queries) - cnt
        