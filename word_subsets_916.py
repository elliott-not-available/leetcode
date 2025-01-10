# https://leetcode.com/problems/word-subsets/?envType=daily-question&envId=2025-01-10
from collections import Counter

class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        words = words1
        substrings = words2
        res = []

        sc = Counter(substrings[0])
        for s in substrings[1:]:
            tc = Counter(s)
            for c in tc:
                if tc[c] > sc[c]:
                    sc[c] = tc[c]

        def check_match(word: Counter, letters: Counter) -> bool:
            for l in letters:
                if word[l] < letters[l]:
                    return False
            return True

        for word in words:
            wc = Counter(word)
            if check_match(wc, sc):
                res.append(word)

        return res
        