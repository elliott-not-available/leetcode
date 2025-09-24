# https://leetcode.com/problems/fraction-to-recurring-decimal/description/?envType=daily-question&envId=2025-09-24

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        res = []
        if (numerator<0) ^ (denominator<0):

            res.append("-")


        top = abs(numerator)
        bot = abs(denominator)

        div = str(top//bot)
        res.append(div)
        rem = top % bot

        if rem == 0:
            return "".join(res)
        
        res.append(".")

        m = {}

        while rem != 0:
            if rem in m:
                res.insert(m[rem], "(")
                res.append(")")
                break

            m[rem] = len(res)
            rem *=10
            res.append(str(rem // bot))
            rem %= bot

        return "".join(res)