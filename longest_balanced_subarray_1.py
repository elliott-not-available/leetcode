# leetcode.com/problems/longest-balanced-subarray-i/?envType=daily-question&envId=2026-02-10

class Solution:
    def longestBalanced(self, nums: list[int]) -> int:

        # distinct even and odd numbers
        n = len(nums)
        res = 0

        for l in range(n-1):
            evens = set()
            odds = set()

            if nums[l] % 2:
                odds.add(nums[l])
            else:
                evens.add(nums[l])

            for r in range(l+1, n):
                
                if nums[r] % 2:
                    odds.add(nums[r])
                else:
                    evens.add(nums[r])

                cur_size = 0

                if len(odds) == len(evens):
                    cur_size = r-l+1

                res = max(res, cur_size)




        return res