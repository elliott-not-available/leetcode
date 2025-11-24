# https://leetcode.com/problems/binary-prefix-divisible-by-5/description/?envType=daily-question&envId=2025-11-24

class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        n = len(nums)
        res = [False] * n

        # # works but time limit exceeded
        # for i in range(1, n+1):

        #     cur_s = "".join(str(s) for s in nums[:i])
        #     cur = int(cur_s, 2)

        #     if cur%5==0:
        #         res[i-1] = True


        # return res

        prefix = 0
        for i in range(n):
            prefix = ((prefix << 1) + nums[i]) % 5
            res[i] = prefix == 0
        return res