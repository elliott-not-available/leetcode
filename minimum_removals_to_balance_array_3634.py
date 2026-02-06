# https://leetcode.com/problems/minimum-removals-to-balance-array/description/?envType=daily-question&envId=2026-02-06

class Solution:
    def minRemoval(self, nums: list[int], k: int) -> int:

        # if len(numbers) == 1:
        #         return 0
        
        # # remove min number of elements so array is ballanced
        # # balanced: max value is <= k*min value

        # numbers = sorted(nums)
        # cur = numbers[-1] / numbers[0]
        # res = 0
        
        # while cur > k:
            
        #     cur = numbers[-1] / numbers[0]
        #     # if not balanced
        #     if cur > k:
        #         # remove end value with greatest impact
        #         end = numbers[-1] - numbers[-2]
        #         start = numbers[2] - numbers[1]

        #         if end > start:
        #             numbers = numbers[:-1]
        #         else:
        #             numbers = numbers[1:]
        #         res += 1

        #     if len(numbers) == 1:
        #         return res
    
        # return res

        n = len(nums)
        numbers = sorted(nums)

        res = n
        r = 0

        for l in range(n):
            while r < n and numbers[r] < numbers[l]*k:
                r += 1
            res = min(res, n - (r-l))
        return res