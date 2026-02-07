# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/?envType=daily-question&envId=2026-02-07

class Solution:
    def minimumDeletions(self, s: str) -> int:

        n = len(s)
        if n == 1:
            return 0

        cur_a = s.count("a")
        cur_b = 0

        res = n

        for i in range(n):
            
            if s[i] == "a":
                cur_a -= 1

            res = min(res, cur_a+cur_b)

            if s[i] == "b":
                cur_b += 1
            

            if cur_a==n or cur_b==n:
                return 0

            # print(s[i], cur_a, cur_b)



        
        return res