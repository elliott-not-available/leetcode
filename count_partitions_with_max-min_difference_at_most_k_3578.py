# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/description/?envType=daily-question&envId=2025-12-06
from sortedcontainers import SortedList

class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        ## DP with prefix 
        n = len(nums)
        MOD = 10**9 +7
        cnt = SortedList()

        dp = [0]*(n+1)
        pref = [0]*(n+1)

        dp[0] = 1
        pref[0] = 1

        j = 0
        for i in range(n):
            cnt.add(nums[i])

            while j >= i and cnt[-1] - cnt[0] > k:
                cnt.remove(nums[j])
                j+= 1

            dp[i+1] = (pref[i+1]- (pref[j-1] if j>0 else 0)) % MOD
            pref[i+1] = (pref[i] + dp[i+1]) % MOD
        return dp[n]
    
        ## can be done with double queue also