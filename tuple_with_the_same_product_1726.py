# https://leetcode.com/problems/tuple-with-same-product/description/?envType=daily-question&envId=2025-02-06

from collections import Counter, defaultdict

class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        # timelimit exceeded

        N = len(nums)
        res_c = defaultdict(int)
        # used = []

        for i in range(N):
            for j in range(i+1, N):
                # if i == j or (i,j) in used or (j,i) in used:
                #     continue
                
                res_c[nums[i]*nums[j]] += 1
                # used.append((i,j))

        # multmap = {1:0}
        # for i in range(2,max(res_c.values())+1):
        #     multmap[i] = 8*(i-1) + multmap[i-1]

        res = 0

        for c in res_c.values():
            if c >= 2:
                # res += multmap[c]
                pairs = (c * (c-1)) // 2
                res += 8 * pairs

        return res
        