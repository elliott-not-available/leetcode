# https://leetcode.com/problems/distribute-candies-among-children-ii/description/?envType=daily-question&envId=2025-06-01

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # # brute force: timelimit exceeded
        # i_r = min(limit, n)
        # res = 0

        # for i in range(i_r+1):
        #     j_r = min(limit, n-i)
        #     for j in range(j_r+1):
        #         k_r = min(limit, n-i-j)
        #         for k in range(k_r+1):
        #             # print(i, j, k)
        #             if i+j+k != n:
        #                 continue
        #             # print("correct: ", i, j, k)
        #             res += 1
                    
        # return res
        ################################################
        # this is the enumeration solution. There is also an Inclusion-Exclusion solution in the editorial (probs more efficient)
        res = 0
        for i in range(min(limit, n)+1):
            res += max(min(limit, n-i) - max(0, n-i-limit)+1, 0)
        return res
