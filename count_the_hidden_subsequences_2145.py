# https://leetcode.com/problems/count-the-hidden-sequences/description/?envType=daily-question&envId=2025-04-21

class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:

        # # bruteforce O(n*(upper-lower))

        # def check_hidden(start):
        #     n = len(differences)
        #     hidden = [0] * (n+1)

        #     hidden[0] = start

        #     for j in range(len(differences)):
        #         hidden[j+1] = hidden[j] + differences[j]

        #         if hidden[j+1] < lower or hidden[j+1] > upper:
        #             return False
        #     return True

        # res = 0

        # for i in range(lower, upper + 1):
        #     if check_hidden(i):
        #         res += 1

        # return res
        #########################################################
        # check min max element with diff array O(n)
        r_limit = upper - lower
        cur_min = 0
        cur_max = 0
        cur = 0
        for d in differences:
            cur += d

            if cur < cur_min:
                cur_min = cur
            if cur > cur_max:
                cur_max = cur

            if cur_max - cur_min > r_limit:
                return 0
        
        r = cur_max - cur_min

        return r_limit - r + 1