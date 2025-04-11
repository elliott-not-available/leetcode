# https://leetcode.com/problems/count-symmetric-integers/description/?envType=daily-question&envId=2025-04-11

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        # brute force O(n * len(str(high)) (high-low loops, then len(str(high)) // 2 loops)
        # base_n = [0] * len(high)
        res = 0

        for i in range(low, high + 1):
            s = str(i)
            S = len(s)
            if S % 2:
                continue

            mid = S // 2

            a = s[:mid]
            b = s[-mid:]
            b_tot = 0
            a_tot = 0

            for c in range(mid):
                a_tot += int(a[c])
                b_tot += int(b[c])      

            # this is slightly slower (almost 200% 550ms to 900ish). not sure why tbh
            # b_tot = sum(int(d) for d in a)
            # a_tot = sum(int(d) for d in b)

            if a_tot == b_tot:
                res += 1

            # print(f"{s}, {a}, {b}")

        return res