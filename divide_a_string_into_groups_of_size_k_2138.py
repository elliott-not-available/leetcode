# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description/?envType=daily-question&envId=2025-06-22

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:

        def ret(inp, k, fill):
            while len(inp) != k:
                inp += fill
            return inp
        i = 0
        res = []

        while i + k <= len(s):
            res.append(s[i:i+k])
            i += k

        if i != len(s):
            res.append(ret(s[i:], k, fill))

        
        return res