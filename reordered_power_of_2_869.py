# https://leetcode.com/problems/reordered-power-of-2/description/?envType=daily-question&envId=2025-08-10

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = str(n)
        limit = 10**9
        data = []
        cur = 1
        i = 0

        while cur < limit:
            cur = 2**i
            data.append(sorted(str(cur)))
            i+=1

        return sorted(s) in data
