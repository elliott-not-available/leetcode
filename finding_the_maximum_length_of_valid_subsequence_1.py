# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/description/?envType=daily-question&envId=2025-07-16

class Solution:
    def maximumLength(self, nums: list[int]) -> int:

        # find max l subsequence where adjacent pairs of values are all odd or all even

        patterns = [[0, 1], [1, 0], [1, 1], [0, 0]]
        res = 0
        
        for pat in patterns:
            cnt = 0

            for n in nums:
                if n % 2 == pat[n%2]:
                    cnt+=1
            res = max(res, cnt)

        return res