# https://leetcode.com/problems/find-the-original-typed-string-i/description/?envType=daily-question&envId=2025-07-01

class Solution:
    def possibleStringCount(self, word: str) -> int:

        res = 0
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                res += 1

        return res