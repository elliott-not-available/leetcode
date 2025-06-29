# uhttps://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/?envType=daily-question&envId=2025-06-29

class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        MOD = 10**9 + 7
        N = len(nums)
        nums.sort()

        power = [1] * N
        for i in range(1, N):
            power[i] = (power[i-1] * 2) % MOD

        l, r = 0, N -1
        res = 0

        while l <= r:
            if nums[l] + nums[r] <= target:
                res = (res + power[r - l]) % MOD
                l += 1
            else:
                r -=1



        return res