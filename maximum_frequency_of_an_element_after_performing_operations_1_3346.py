# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/?envType=daily-question&envId=2025-10-21

class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:

        ## Brute force, think there is an index error somewhere
        # nums.sort()
        # n = len(nums)

        # max_cnt = 0

        # for i in len(n):
        #     cur_ops = numOperations
        #     cur_cnt = 0
        #     for j in range(n):
        #         if i==j:
        #             continue

        #         dif = abs(nums[i] - nums[j])

        #         if dif == 0:
        #             cur_cnt += 1
        #         elif dif <= k and cur_ops > 0:
        #             cur_cnt += 1
        #             cur_ops -= 1

        #     max_cnt = max(max_cnt, cur_cnt)
        
        # return max_cnt

        max_v = max(nums) + k + 2
        count = [0] * max_v

        for n in nums:
            count[n] += 1

        # cumulative count
        for i in range(1, max_v):
            count[i] += count[i-1]


        res = 0

        for i in range(max_v):
            l = max(0, i-k)
            r = min(max_v-1, i+k)

            tot = count[r] - (count[l-1] if l else 0)
            freq = count[i] - (count[i-1] if i else 0)

            res = max(res, freq + min(numOperations, tot-freq))

        return res