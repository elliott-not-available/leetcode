# https://leetcode.com/problems/delete-columns-to-make-sorted/?envType=daily-question&envId=2025-12-20

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs[0])
        cols = [[] for _ in range(n)]

        for s in strs:
            for i in range(n):
                
                cols[i].append(s[i])
                # print(i, cols, s, n)

        res = 0

        for c in cols:
            sorted_col = sorted(c)
            # print(c, sorted_col)

            if c != sorted_col:
                res += 1

        return res
        