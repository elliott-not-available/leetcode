# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

# from collections import Counter
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # n = len(s)
        # r = n-1

        # for i in range(n):
        #     while r > i+1:
        #         if s[i] == s[r]:
        #             res += len(Counter(s[i+1:r-1]).keys())
        letters = set(s)
        res = 0
        for l in letters:
            i, j = s.index(l), s.rindex(l)
            bet = set()

            for k in range(i+1, j):
                bet.add(s[k])

            res += len(bet)
                
        return res