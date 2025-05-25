# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/?envType=daily-question&envId=2025-05-25
from collections import defaultdict, Counter

class Solution:
    def longestPalindrome(self, words: list[str]) -> int:

        # # if even max pairs
        # # if odd pairs + 1 double

        # cntr = defaultdict(int)
        # pairs = 0
        # doubles = defaultdict(int)
        # c = 0

        # for w in words:
        #     # store doubles
        #     if w[0] == w[1]:
        #         c += 1
        #         doubles[w] += 1

        #     # store word
        #     cntr[w] += 1

        #     # if pair exists in d
        #     # increment pair, remove 1 of both from d
        #     if cntr[w[::-1]] > 0:
        #         # print(w)
        #         # print(pairs)
        #         # print(cntr)
        #         if w[0] != w[1]:
        #             pairs += 1
        #             cntr[w] -= 1
        #             cntr[w[::-1]] -= 1
        #         else:

        #             if cntr[w] >= 2:
        #                 pairs +=1
        #                 cntr[w] -= 2
        #                 doubles[w] -= 2
        #                 c -= 2
        # # print(pairs)
        # # print(cntr)

        # return pairs*4 + 2 if c else pairs*4
        ##################################################
        # 
        cntr = Counter(words)
        leftover = False
        res = 0

        for w, cnt in cntr.items():

            bkw = w[::-1]

            if bkw == w:

                if cnt % 2 == 0:
                    res += cnt
                else:
                    leftover = True
                    res += cnt - 1

            # < so you dont do it twice
            elif w < bkw:
                res += 2*min(cnt, cntr[bkw])

        if leftover:
            res += 1

        return 2 * res
            
