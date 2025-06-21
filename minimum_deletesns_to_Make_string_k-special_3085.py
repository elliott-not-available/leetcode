# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/description/?envType=daily-question&envId=2025-06-21
from collections import Counter
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:

        # word is k-special if |freq(word[i]) - freq(word[j])| <= k
        c = Counter(word)
        res = len(word)

        # for i in letters:
        #     for j in letters:

        #         if i == j: continue

                
        #         i_c = c[i]
        #         j_c = c[j]

        #         temp = abs(i_c - j_c)

        #         while temp > k:
        #             temp -= 1
        #             res += 1

        #             if i_c < j_c:
        #                 c[i] -= 1
        #             else:
        #                 c[j] -= 1
        # return res

        for a in c.values():
            deleted = 0
            for b in c.values():
                if a > b:
                    deleted += b
                elif b > a + k:
                    deleted += b - (a+k)
                
            res = min(res, deleted)
        return res
                




