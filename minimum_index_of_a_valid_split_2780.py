# https://leetcode.com/problems/minimum-index-of-a-valid-split/description/?envType=daily-question&envId=2025-03-27

from collections import defaultdict, Counter

class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        
        left = defaultdict(int)
        right = Counter(nums)

        for i in range(len(nums)):
            left[nums[i]] += 1
            right[nums[i]] -= 1

            left_len = i + 1
            right_len = len(nums) -i -1

            if 2 * left[nums[i]] > left_len and 2 * right[nums[i]] > right_len:
                return i 
        
        return -1