# https://leetcode.com/problems/count-operations-to-obtain-zero/description/?envType=daily-question&envId=2025-11-09

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        
        # # brute force loop
        # res = 0
        # while num1 > 0 and num2 > 0:
        #     if num1 >= num2:
        #         num1 -= num2
        #     else:
        #         num2 -= num1
        #     res += 1
        # return res

        # euclidean subtraction method?

        res = 0

        while num1 and num2:
            res += num1 // num2
            num1 %= num2
            num1, num2 = num2, num1
        return res