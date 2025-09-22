# https://leetcode.com/problems/count-elements-with-maximum-frequency/?envType=daily-question&envId=2025-09-22

from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        # counter.most_common() uses a heap
        c = Counter(nums)
        s = c.most_common()
        res = s[0][1]
        prev = s[0][1]

        for v in s[1:]:
            if v[1] != prev:
                return res
            
            res += v[1] 

        return res
        