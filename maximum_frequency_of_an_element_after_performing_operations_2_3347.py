#https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/description/?envType=daily-question&envId=2025-10-22
from collections import Counter
from bisect import bisect_left, bisect_right
class Solution:

    def max_freq_of_array(self, nums, k, numOperations):
            count = Counter(nums)

            res = 0

            for v in count.keys():
                l = bisect_left(nums, v-k)
                r = bisect_right(nums, v+k) - 1

                freq = min(r-l+1, numOperations + count[v])
                res = max(res, freq)

            return res

    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:

        nums.sort()
        arr_max_freq = self.max_freq_of_array(nums, k, numOperations)

        left = 0
        other = 0

        for right in range(len(nums)):

            while nums[right] > nums[left] + 2*k:
                left += 1
            
            other = max(other, right-left + 1)

            if other >= numOperations:
                other = numOperations
                break

        return max(arr_max_freq, other)
        