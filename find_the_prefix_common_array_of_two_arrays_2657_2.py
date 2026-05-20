# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/?envType=daily-question&envId=2026-05-20

class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        
        n = len(A)
        res = [0]*n

        in_a = set()
        in_b = set()

        for i in range(n):
            in_a.add(A[i])
            in_b.add(B[i])

            c = 0

            for e in in_a:
                if e in in_b:
                    c += 1
            
            res[i] = c
        
        return res