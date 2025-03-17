# https://leetcode.com/problems/zero-array-transformation-ii/?envType=daily-question&envId=2025-03-13

class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        # brute force - timelimit exceeded

        # aim = [0] * len(nums)
        # in_use_nums = nums.copy()
        # cnt = 0

        # for q in queries:
        #     if in_use_nums == aim:
        #         return cnt
        #     l, r, v = q
        #     cnt += 1
        #     for i in range(l, r+1):
        #         if in_use_nums[i] <= v:
        #             in_use_nums[i] = 0
        #         else:
        #             in_use_nums[i] -= v

        # return cnt if in_use_nums == aim else -1
        

        # editorial solution - called a line sweep
        N = len(nums)
        total_sum = 0
        k = 0
        diff_arr = [0] * (N+1)

        for i in range(N):

            while total_sum + diff_arr[i] < nums[i]:
                k += 1

                if k > len(queries):
                    return -1
                
                l, r, v = queries[k-1]

                if r >= i:
                    diff_arr[max(l, i)] += v
                    diff_arr[r + 1] -= v

                total_sum += diff_arr[i]

        return k