# https://leetcode.com/problems/maximum-69-number/description/?envType=daily-question&envId=2025-08-16

class Solution:
    def maximum69Number (self, num: int) -> int:
        str_rpr = str(num)
        res = [s for s in str_rpr]
        for i in range(len(str_rpr)):
            if str_rpr[i] == "6":
                res[i] = "9"
                return int("".join(n for n in res))
        return num