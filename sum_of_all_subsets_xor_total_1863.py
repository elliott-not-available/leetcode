# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/?envType=daily-question&envId=2025-04-05

# from functools import reduce
# from operator import xor

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:


        # # AHHH it is subSET not subARRAY (subset is not contiguous), oh nvm i am now confused?
        # # brute force o(n**2)
        # res = 0
        # N = len(nums)

        # for i in range(N):
        #     cur = i
        #     for j in range(i+1, N):
        #         print(f"{i} to {j}")
        #         cur = cur ^ nums[j]
        #         # res += reduce(xor, map(int, nums[i:j]))
        #         res += cur

        # return res

        # # dfs recursive o(2**n)

        # def dfs(i, total):

        #     if i == len(nums):
        #         return total
            
        #     return dfs(i+1, total ^ nums[i]) + dfs(i+1, total)
        
        # return dfs(0,0)

        # some maths soltion o(n)

        # if atleast one bit is set then it will turn up in half the solutions
        # there are 2**n solutions

        # 1. get all set bits with or
        # 2. multiply that by 2**(n-1) (half total solutions)

        res = 0

        for n in nums:
            res = res | n

        return res * (2**(len(nums) - 1))
        
