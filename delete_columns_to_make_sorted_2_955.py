# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/?envType=daily-question&envId=2025-12-21

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n, m = len(strs), len(strs[0])
        sorted_paris = [False] * (n-1)

        res = 0

        for c in range(m):
            bad = False

            for i in range(n-1):
                if not sorted_paris[i] and strs[i][c] > strs[i+1][c]:
                    bad = True
                    break

            if bad:
                res += 1
                continue

            for i in range(n-1):
                if not sorted_paris[i] and strs[i][c] < strs[i+1][c]:
                    sorted_paris[i] = True

            if all(sorted_paris):
                break

        return res