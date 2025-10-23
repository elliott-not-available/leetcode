# tshttps://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/?envType=daily-question&envId=2025-10-23

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        new = s
        cur = s
        while len(cur) > 2:
            new = [((int(cur[int(i)]) + int(cur[int(i+1)])) % 10) for i in range(len(cur)-1)]
            # print(new)
            cur = new
        return cur[0] == cur[1]