# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/?envType=daily-question&envId=2025-09-13
from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vs = 'aeiou'

        vowel_count = Counter()
        cons_count = Counter()

        for c in s:
            if c in vs:
                vowel_count[c] += 1
            else:
                cons_count[c] += 1

        v, c = 0, 0
        if vowel_count:
            v = vowel_count.most_common(1)[0][1]
        if cons_count:
            c = cons_count.most_common(1)[0][1]

        return v+c