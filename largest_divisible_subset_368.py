# https://leetcode.com/problems/largest-divisible-subset/description/?envType=daily-question&envId=2025-04-06

class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:

        N = len(nums)

        def is_factor(a, b):
            if a % b == 0 or b % a == 0:
                return True
            return False
        
        def is_factor_strict(smaller, larger):
            if (larger % smaller == 0):
                return True
            return False

        ## try brute force first (is kinda greedy) - does not work

        # max = []

        # for i in range(N):

        #     cur = nums[i]
        #     temp = [cur]

        #     for j in range(i+1, N):
        #         next = nums[j]

        #         # # greedy approach is not working (logic is incorrect)
        #         # # if base mode new == 0, NEW smaller than base
        #         # if largest_cur % next == 0:
        #         #     temp.append(next)

        #         # # if new mode base == 0, BASE smaller then new
        #         # elif next % largest_cur == 0:
        #         #     temp.append(next)
        #         #     largest_cur = next

        #         works = True
        #         for t in temp:

        #             if not (t % next == 0 or next % t == 0):
        #                 works = False
                        
        #         if works:
        #             temp.append(next)
                    
        #     if len(temp) > len(max):
        #         max = temp

        # return max

        #################################################################

        # # try include/ignore tree - works but seems only just

        
        
        # # i think my above solution might have worked if i sorted nums
        # nums.sort()
        # cache = {}

        # def dfs(i, prev):
        #     if i == N:
        #         return []
        #     if (i, prev) in cache:
        #         return cache[(i, prev)]
            
        #     # skip
        #     res = dfs(i+1, prev)

        #     # include
        #     if is_factor(prev, nums[i]):
        #         tmp = [nums[i]] + dfs(i+1, nums[i])

        #         if len(tmp) > len(res):
        #             res = tmp

        #     cache[(i, prev)] = res
            
        #     return res
        
        # return dfs(0, 1)

        #################################################################

        # ingore/include but with less space taken up

        # nums.sort()
        # cache = {}

        # def dfs(i):
        #     if i == len(nums):
        #         return []
        #     if i in cache:
        #         return cache[i]
            
        #     res = [nums[i]]

        #     for j in range(i+1, N):

        #         if is_factor(nums[i], nums[j]):
        #             tmp = [nums[i]] + dfs(j)

        #             if len(tmp) > len(res):
        #                 res = tmp

        #     cache[i] = res

        #     return res

        # res = []

        # for i in range(N):
        #     tmp = dfs(i)
        #     if len(tmp) > len(res):
        #         res = tmp


        # return res

        #################################################################

        # tabulation - fill in from the end

        nums.sort()
        dp = [[n] for n in nums] # dp[i] longest seq starting at i
        res = dp[0]

        for i in reversed(range(N)):
            for j in range(i+1, N):

                if is_factor_strict(smaller=nums[i], larger=nums[j]):
                    tmp = [nums[i]] + dp[j]

                    if len(tmp) > len(dp[i]):
                        dp[i] = tmp

                if len(dp[i]) > len(res):
                    res = dp[i]

        return res