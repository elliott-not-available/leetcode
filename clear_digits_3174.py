# https://leetcode.com/problems/clear-digits/description/?envType=daily-question&envId=2025-02-10

class Solution:
    def clearDigits(self, s: str) -> str:
        N = len(s)
        res = []

        for i in range(N):
            if s[i].isnumeric():
                res = res[:-1]
            else:
                res.append(s[i])

        return "".join(res)