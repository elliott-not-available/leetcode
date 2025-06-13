# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/?envType=daily-question&envId=2025-06-13

class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        # if p == 0:
        #     return p
        # # brute force, can be optimised with a heap
        # n = len(nums)
        # dif_data = []

        # for i in range(n):
        #     for j in range(n):

        #         if i == j: continue

        #         dif_data.append(abs(nums[i] - nums[j]))

        # a = sorted(dif_data)

        # # print(a)
        # # print(a[:p])
        
        # # *2 to deal with i,j / j,i
        # return max(a[:p*2])
        ###########################################################
        if p == 0:
            return p
        
        s_nums = sorted(nums)
        n, l, r = len(nums), 0, s_nums[-1] - s_nums[0]

        while l < r:
            m, pairs = l + (r-l)//2, 0
            i = 1

            while i < n:
                if s_nums[i] - s_nums[i-1] <= m:
                    pairs += 1
                    i += 1
                i += 1

            if pairs >= p:
                r = m
            else:
                l = m + 1
        return l

        