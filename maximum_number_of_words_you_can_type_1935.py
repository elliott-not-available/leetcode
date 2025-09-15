# https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/?envType=daily-question&envId=2025-09-15

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        for w in text.split(" "):
            keys_work = True
            for l in brokenLetters:
                if l in w:
                    keys_work = False
                    break
            if keys_work:
                res += 1
        return res