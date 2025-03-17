# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/?envType=daily-question&envId=2025-01-04

class Solutio_og:
    # brute force - timelimit exceed
    def countPalindromicSubsequence(self, s: str) -> int:
        N = len(s)
        def is_palindrome(input: str) -> bool:
            # for i in range(N//2):
            #     if input[i] != input[-(i+1)]:
            #         return False
            # return True
            if input[0] == input[-1]:
                return True
            return False
        
        res = []

        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    cur_s = s[i]+s[j]+s[k]

                    if cur_s in res:
                        continue

                    if is_palindrome(cur_s):
                        res.append(cur_s)

        return len(res)
    
from collections import defaultdict, Counter

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        m = 1
        l = set()
        r = Counter(s)

        uni = set()

        for m in s:
            r[m] -= 1

            for c in l:
                if r[c] > 0:
                    uni.add((m, c))

            l.add(m)
            
        return len(uni)