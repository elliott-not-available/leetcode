# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/?envType=daily-question&envId=2026-02-26
# import math
class Solution:
    def numSteps(self, s: str) -> int:

        n = int(s, 2)
        res = 0
        # print(n)
        while n!=1:
            if n&1:
                n+=1
            else:
                n>>=1
            res += 1

        return res

        ## wrong
        # res = 0
        # n = len(s)

        # for i in range(n-1, -1, -1):
            
        #     if i == n-1:
        #         if s[i] == "1":
        #             print("end: ", i)
        #             res += 1
        #     else:
        #         if s[i] == "1":
        #             print("middle: ", i)
        #             res += (n-1-i) 
        # # -1, -2, -3, -4, -5
        # # 1,   1,  2,  3,  4 
        # return res