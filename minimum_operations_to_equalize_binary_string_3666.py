# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/description/?envType=daily-question&envId=2026-02-27
import math
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        # it is exactly k flips not min
        # zero = s.count("0")
        # return zero if zero <=k else -1

        zeros = s.count("0")
        len_s = len(s)

        if zeros==0: return 0
        # ??
        if len_s==k:
            # return ((1 if zeros==len_s else 0) << 1) - 1
            
            # 1 if all 0s
            # 0 if all 1s
            # -1 else
            # if len_s==zeros:
            #     return 1
            # if zeros==0: # not needed because above
            #     return 0
            # return -1
            return 1 if zeros==len_s else -1
        
        base = len_s - k

        odd = int(max(math.ceil(float(zeros)/k), math.ceil(float(len_s-zeros)/base)))
        even = int(max(math.ceil(float(zeros)/k), math.ceil(float(zeros)/base)))

        
        # if odd is even => adds one, if odd is odd => adds 0
        odd += ~odd&1 
        even += even&1 #if even is even => add 0, if even is odd => add 1

        res = float("inf")

        if (k&1) == (zeros&1):
            res = min(res, odd)

        if (~zeros & 1):
            res = min(res, even)

        if res==float("inf"):
            res = -1

        return res


