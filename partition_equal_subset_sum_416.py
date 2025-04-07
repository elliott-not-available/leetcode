# https://leetcode.com/problems/partition-equal-subset-sum/description/?envType=daily-question&envId=2025-04-07

class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        # # greedy 2pointer approach, doesnt quite seem to work
        # # ( for example [2, 2, 1, 1] it can not find a solution)

        # N = len(nums)
        # if N == 1:
        #     return False

        # nums.sort()
        # bot, top = 0, 0
        # i, j = 0, N - 1

        # while i <= j:
        #     if bot < top:
        #         print(f"bot smaller: {i}, {j}, {bot}, {top}")
        #         bot += nums[i]
        #         i += 1
        #     elif bot > top:
        #         print(f"top smaller: {i}, {j}, {bot}, {top}")
        #         top += nums[j]
        #         j -= 1
        #     elif bot == top:
        #         if i == j:
        #             return False
        #         print(f"equal: {i}, {j}, {bot}, {top}")
        #         bot += nums[i]
        #         top += nums[j]
        #         i += 1
        #         j -= 1
        # return bot == top
        ######################################################
        ## include ignore tree for bot - timelimit exceeded
        ## return  true if sum(nums) - ans

        ## could cache something maybe?
        # tot = sum(nums)

        # def dfs(i, cur):
        #     if i > len(nums) - 1:
        #         return cur == (tot - cur)
            
        #     if cur > (tot - cur):
        #         return False
        #     elif cur == (tot - cur):
        #         return True
            
        #     a = dfs(i+1, cur+nums[i])
        #     b = dfs(i+1, cur)

        #     if any([a, b]):
        #         return True
        #     return False
        
        # return dfs(0, 0)
        ######################################################
        # gather unique combs, if one = tot/2 return True

        tot = sum(nums)

        if tot % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in reversed(range(len(nums) - 1)):
            nextDP = set()
            for t in dp:

                n = t+nums[i]
                if n == target:
                    return True
                
                nextDP.add(n)
                nextDP.add(t)

            dp = nextDP
        
        return False
            

