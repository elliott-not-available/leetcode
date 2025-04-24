# https://leetcode.com/problems/count-largest-group/?envType=daily-question&envId=2025-04-23

from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:

        # max logic is wrong somewhere
        # if n == 1:
        #     return 1

        # cntr = defaultdict(int)
        # cur_max = 0
        # max_cnt = 0
        # for i in range(1, n):

        #     s = sum([int(c) for c in str(i)])
        #     cntr[s] += 1

        #     if cntr[s] > cur_max:
        #         cur_max = cntr[s]
        #         max_cnt = 1
            
        #     if cntr[s] == cur_max:
        #         max_cnt += 1

        
        # return max_cnt
        ##########################################
        if n == 1:
            return 1

        cntr = defaultdict(int)

        for i in range(1, n+1):

            s = sum([int(c) for c in str(i)])
            cntr[s] += 1

        max_v = max(cntr.values())
        c = sum(1 for v in cntr.values() if v == max_v)

        print(cntr)
        return c