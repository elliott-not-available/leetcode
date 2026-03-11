# https://leetcode.com/problems/complement-of-base-10-integer/description/?envType=daily-question&envId=2026-03-11
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        b = bin(n)[2:]
        res = ""
        for c in b:
            if c=="1":
                res += "0"
            if c=="0":
                res += "1"


        return int(res, 2)