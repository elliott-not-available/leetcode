# https://leetcode.com/problems/count-binary-substrings/description/?envType=daily-question&envId=2026-02-19

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # # 2pntr with cnt map (answering the wrong question)
        # n = len(s)
        # used = set()
        # res = 0


        # for i in range(n):
        #     c_map = {
        #         "0":0,
        #         "1":0,
        #         }
        #     for j in range(i,n):
        #         c_map[s[j]] += 1

        #         if c_map["0"] == c_map["1"] and (i,j) not in used:
        #             used.add((i, j))
        #             res += 1

        # return res

        # ALL 0/1's GROUPED CONSECUTIVELY

        res, prev, cur = 0, 0, 1

        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                res += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1
        return res + min(prev, cur)