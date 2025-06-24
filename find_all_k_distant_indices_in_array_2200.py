# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/description/?envType=daily-question&envId=2025-06-24

class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:

        # # enumeration
        # N = len(nums)
        # res = []
        
        # for i in range(N):
        #     for j in range(N):
        #         if nums[j] == key and abs(i - j) <= k:
        #             res.append(i)
        #             break

        # return res
        ###################################################
        r = 0
        res = []
        N = len(nums)

        for j in range(N):
            if nums[j] == key:
                l = max(r, j-k)
                r = min(N-1, j+k) + 1
                for i in range(l,r):
                    res.append(i)

        return res