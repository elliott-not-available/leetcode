# https://leetcode.com/problems/count-partitions-with-even-sum-difference/description/?envType=daily-question&envId=2025-12-05

class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        ## sim
        # l = 0
        # r = sum(nums)
        # res = 0

        # for n in nums[:-1]:
        ##     print(n)
        #     l += n
        #     r -= n

        #     dx = abs(r-l)
        #     if dx%2==0:
        #         res += 1

        # return res
        return len(nums)-1 if sum(nums)%2==0 else 0