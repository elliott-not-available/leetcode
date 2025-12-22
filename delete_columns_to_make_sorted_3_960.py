# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/?envType=daily-question&envId=2025-12-22

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:

        n = len(strs[0])
        mm = [1] * n

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):

                if all(row[i] <= row[j] for row in strs):
                    mm[i] = max(mm[i], 1 + mm[j])


        return n - max(mm)