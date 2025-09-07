# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/?envType=daily-question&envId=2025-09-07

class Solution:
    def sumZero(self, n: int) -> list[int]:
        res = []
        if n % 2: res.append(0)

        for i in range(1, (n//2)+1):
            res.append(i)
            res.append(-i)

        return res
        