# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/?envType=daily-question&envId=2025-03-11

from collections import Counter, defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # # brute force O(n**2)
        # N = len(s)

        # def check_cntmap():
        #     if len(cntmap) < 3:
        #         return False
        #     for k in cntmap:
        #         if cntmap[k] < 1:
        #             return False
        #     return True

        # res = 0

        # for i in range(N):
        #     for j in range(i+1, N+1):
        #         cur = s[i:j]
        #         cntmap = Counter(cur)

        #         if check_cntmap():
        #             print(cur)
        #             res += 1
                
        # return res
        res = 0
        l = 0
        # cntmap = defaultdict(int)
        cntmap = [0] * 3
        N = len(s)

        def get_ord(char):
            return ord(char) - ord("a")

        for r in range(N):
            cntmap[get_ord(s[r])] += 1

            while cntmap[0] and cntmap[1] and cntmap[2]:
                res += (N - r)
                cntmap[get_ord(s[l])] -= 1
                l += 1             

        return res