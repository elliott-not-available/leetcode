# https://leetcode.com/problems/counting-words-with-a-given-prefix/description/?envType=daily-question&envId=2025-01-09

class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        res = 0

        for w in words:
            if w.startswith(pref):
                res += 1

        return res 
        