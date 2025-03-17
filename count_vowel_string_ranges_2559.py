# https://leetcode.com/problems/count-vowel-strings-in-ranges/?envType=daily-question&envId=2025-01-02
from functools import cache

class Solution_og:
    # bm and sum_bm - seems to be about as inefficient as it can be without failing haha
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        @cache
        def conditions(word: str) -> int:
            vowels = ["a", "e", "i", "o", "u"]
            if word[0] in vowels and word[-1] in vowels:
                return 1
            return 0
        
        bm = [conditions(w) for w in words]
        sum_bm = [bm[0]]
        for i in range(1,len(bm)):
            sum_bm.append(sum_bm[-1] + bm[i])

        @cache
        def gen_res(start: int, end: int) -> int:
            if start == 0:
                return sum_bm[end]
            return sum_bm[end] - sum_bm[start-1]

        res = [gen_res(start, end) for start, end in queries]

        return res
    

# https://leetcode.com/problems/count-vowel-strings-in-ranges/?envType=daily-question&envId=2025-01-02
from functools import cache

class Solution:
    # haha tried to optimise and it got slower
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        @cache
        def conditions(word: str) -> int:
            vowels = set("aeiou")
            if word[0] in vowels and word[-1] in vowels:
                return 1
            return 0
        
        n_w = len(words)
        sum_bm = [0] * n_w
        sum_bm[0] = conditions(words[0])

        for i in range(1,n_w):
            sum_bm[i] = sum_bm[i-1] + conditions(words[i])

        @cache
        def gen_res(start: int, end: int) -> int:
            if start == 0:
                return sum_bm[end]
            return sum_bm[end] - sum_bm[start-1]

        res = [gen_res(start, end) for start, end in queries]

        return res