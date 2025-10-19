# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/?envType=daily-question&envId=2025-10-19
import math
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        # visited = [False] * n
        res = s
        s = s + s
        i = 0

        # while not visited[i]:
        #     visited[i] = True
        g = math.gcd(b, n)
        for i in range(0, n, g):
            for j in range(10):
                k_lim = 0 if b % 2 == 0 else 9
                for k in range(k_lim+1):

                    t = list(s[i : i+n])
                    for p in range(1, n, 2):
                        t[p] = str((int(t[p]) + j*a) % 10)
                    for p in range(0, n, 2):
                        t[p] = str((int(t[p]) + k*a) % 10)

                    t_str = "".join(t)
                    if t_str < res:
                        res = t_str

        return res