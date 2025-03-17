# https://leetcode.com/problems/string-matching-in-an-array/?envType=daily-question&envId=2025-01-07


class Solution:
    # optimised by sorting words list by length of word, and then  second loop starts at i+1
    def stringMatching(self, words: list[str]) -> list[str]:
        words.sort(key=len)
        # print(words)
        res = []

        for i, w in enumerate(words):
            for j in range(i+1, len(words)):
                if w in words[j]:
                    res.append(w)
                    break

        return res
        