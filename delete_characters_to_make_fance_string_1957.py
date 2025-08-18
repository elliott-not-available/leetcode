# https://leetcode.com/problems/delete-characters-to-make-fancy-string/submissions/1705574596/?envType=daily-question&envId=2025-07-21

class Solution:
    def makeFancyString(self, s: str) -> str:

        res = s[0]
        prev = s[0]  
        freq = 1

        for i in range(1, len(s)):
            cur = s[i]
            if cur == prev:
                freq +=1

            if freq < 3:
                res += cur

            prev = cur

        return res