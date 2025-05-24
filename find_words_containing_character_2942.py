# https://leetcode.com/problems/find-words-containing-character/description/?envType=daily-question&envId=2025-05-24

class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        res = []

        for i, w in enumerate(words):

            if x in w:
                res.append(i)
                continue
        
        return res