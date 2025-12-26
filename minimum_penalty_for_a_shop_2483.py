# https://leetcode.com/problems/minimum-penalty-for-a-shop/description/?envType=daily-question&envId=2025-12-26

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # return earliest close hour that minimises penalty
        # open and N
        # closed and Y
        
        pen = customers.count("Y")

        res = 0
        pre_min = pen

        for i in range(len(customers)):

            c = customers[i]

            if c == "Y":
                pen -= 1
            elif c == "N":
                pen += 1

    

            if pen < pre_min:
                pre_min = pen
                res = i + 1



        return res