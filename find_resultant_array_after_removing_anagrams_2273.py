# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/?envType=daily-question&envId=2025-10-13
from collections import Counter
class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        
        res = [words[0]]
        prev = Counter(words[0])

        for w in words[1:]:
            c = Counter(w)
            if c != prev:
                res.append(w)
            prev = c

        return res