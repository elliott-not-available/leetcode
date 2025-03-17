# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/?envType=daily-question&envId=2025-02-12

# import heapq
# import math

class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        # same divisor
        # maximum sum

        # could optimise by caching divisors of needed digits and checking union 
        # wait is this even needed?
        # def check_divs(a, b) -> bool:
        #     res = math.gcd(a, b)

        #     if res != 1:
        #         return True
        #     return False
        
        def digit_sum(a) -> int:
            digit_sum = 0
            str_a = str(a)

            for c in str_a:
                digit_sum += int(c)
            return digit_sum
        
        N = len(nums)
        nums = sorted(nums, reverse=True)

        digit_sums = []
        for i in nums:
            digit_sums.append(digit_sum(i))

        # sums = []
        # heapq.heapify(sums)

        for i in range(N):
            for j in range(i+1, N):

                if digit_sums[i] == digit_sums[j]:
                    s = nums[i]+nums[j]# * -1
                    # heapq.heappush(sums, (s, i, j))
                    return s


        # while sums:

        #     val, i, j = heapq.heappop(sums)
        #     val = -1 * val

        #     # if check_divs(nums[i], nums[j]):
        #     #     return val
        #     return val

        return -1

import heapq

class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        
        def get_digit_sum(a) -> int:
            digit_sum = 0
            str_a = str(a)

            for c in str_a:
                digit_sum += int(c)
            return digit_sum
        
        digit_sums = [[] for _ in range(82)]
        max_pair = -1

        for n in nums:
            digit_sum = get_digit_sum(n)
            heapq.heappush(digit_sums[digit_sum], n)

            if len(digit_sums[digit_sum]) > 2:
                heapq.heappop(digit_sums[digit_sum])

        for min_heap in digit_sums:
            if len(min_heap) == 2:
                first = heapq.heappop(min_heap)
                second = heapq.heappop(min_heap)
                max_pair = max(max_pair, first+second)

        return max_pair