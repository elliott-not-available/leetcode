#https://leetcode.com/problems/zero-array-transformation-i/description/?envType=daily-question&envId=2025-05-20

class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        # # brute force: O(q + sum(length_of_queries) + N) - timelimit exceeded
        # N = len(nums)
        # query_adjust = [0] * N

        # for l, r in queries:

        #     for i in range(l, r+1):
        #         query_adjust[i] += 1

        
        # return all([(nums[i] - query_adjust[i] <= 0) for i in range(N)])
        #################################################
        # difference array: O(3N)

        N = len(nums)
        build_adjust = [0] * (N+1)
        for l, r in queries:
            build_adjust[l] += 1
            build_adjust[r+1] -= 1

        adjust = []
        cur_adjust = 0

        for a in build_adjust:
            cur_adjust += a
            adjust.append(cur_adjust)

        for i in range(N):
            if adjust[i] < nums[i]:
                return False
            
        return True