# https://leetcode.com/problems/vowel-spellchecker/?envType=daily-question&envId=2025-09-14
from typing import List
# from collections import defaultdict

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # doesnt actually pass the test, can not find problem tho
        vowels = 'aeiouAEIOU'

        def replace_vowels(word):
            return "".join("*" if c in vowels else c for c in word)
        
        exact = set(wordlist)
        # words_lower = defaultdict(str)
        # words_novowels = defaultdict(str)
        words_lower = {}
        words_novowels = {}

        for w in wordlist:
            words_lower.setdefault(w.lower(), w)
            words_novowels.setdefault(replace_vowels(w), w)

        def find_match(q):

            if q in exact:
                return q
            
            if q.lower() in words_lower:
                return words_lower[q.lower()]
            
            q_replace_vowels = replace_vowels(q)

            if q_replace_vowels in words_novowels:
                return words_novowels[q_replace_vowels]

            return ""            

        res = []
        for q in queries:
            res.append(find_match(q))

        return res