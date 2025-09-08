# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/description/?envType=daily-question&envId=2025-09-08

class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:



        for i in range(n):
            s = i
            e = n-i

            if "0" in str(s) or "0" in str(e):
                continue
            return [s, e]

        # if str(n).endswith("1"):
        #     return [2, n-2]
        # else:
        #     return [1, n-1]

        # return [1, n-1]