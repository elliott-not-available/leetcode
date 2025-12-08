# https://leetcode.com/problems/count-square-sum-triples/description/?envType=daily-question&envId=2025-12-08
from math import sqrt
class Solution:
    def countTriples(self, n: int) -> int:
        res = 0

        for i in range(1, n):
            for j in range(1, n):
                if i==j:
                    continue

                k = int(sqrt(i**2 + j**2))

                if k<=n and k**2==(i**2 + j**2):
                    # print(i, j, k)
                    res +=1

        # Euclid's Formula | Generate Pythagorean Triples is faster
        return res