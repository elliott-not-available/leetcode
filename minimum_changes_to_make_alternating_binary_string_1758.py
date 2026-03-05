# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/?envType=daily-question&envId=2026-03-05

class Solution:
    def minOperations(self, s: str) -> int:

        res_a = 0
        res_b = 0

        for i in range(len(s)):

            if i%2==0:
                if s[i] =="0":
                    res_b += 1
                else:
                    res_a += 1
            else:
                if s[i] =="1":
                    res_b += 1
                else:
                    res_a += 1

        return min(res_a, res_b)