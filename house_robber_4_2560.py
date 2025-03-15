# https://leetcode.com/problems/house-robber-iv/description/?envType=daily-question&envId=2025-03-15

class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:

        # want to minimise result when chosing perm of 2 nums in nums where you max(choic 1, choice 2)
        # can not chose adjacent

        # min_1 = float("inf")
        # min_2 = float("inf")

        # sorted_nums = sorted(nums)

        # for i in range(len(nums)):

        # so he has to rob k houses, but they can not be adjacent
        # can use double loop starting j at i + 2
        # i - x will just be repeats
        # this would only work for k=2 tho

        # def choose_next(current_index: int) -> int:
        #     return current_index + 2
        
        # choices = []

        # for i in range(len(nums)):
        #     cur = [i]
        #     cur_k = k

        #     while cur_k > 1:
        #         nxt = choose_next(cur[-1])
        #         cur.append(nxt)

        #     # nah this is deffo wrong, not chosing all choices of house, being retarded


        # brute force: 
        # 1. get all perms -> tree
        # 2. store / update min result
        # 3. return res

        # backtracking: tree with 2 choices -> works but memory limit exceeded
        # cache = {}
        # def backtrack(i, k):
            
        #     if i >= len(nums):
        #         if k:
        #             return float("inf")
        #         return 0
            
        #     if (i, k) in cache:
        #         return cache[(i,k)]
            
        #     res1 = max(nums[i], backtrack(i+2, k-1))
        #     res2 = backtrack(i+1, k)

        #     res = min(res1, res2)

        #     cache[(i, k)] = res
        #     return res

        # return backtrack(0, k)
        

        # binary search - range

        def is_valid(cap):
            i = 0
            cnt = 0

            while i < len(nums):
                if nums[i] <= cap:
                    i +=2
                    cnt += 1
                else:
                    i += 1
                if cnt == k:
                    break
            return cnt == k

        l = min(nums)
        r = max(nums) # n
        res = 0
        
        while l <= r:
            m = (l+r) // 2

            if is_valid(m):
                res = m
                r = m - 1
            else:
                l = m + 1

        return res