# https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/description/?envType=daily-question&envId=2025-07-12
from functools import cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:

        @cache
        def dp(n, f, s):
            if f+s == n+1:
                return (1,1)
            
            if f+s > n+1:
                return dp(n, n+1-s, n+1-f)
            
            ealiest, latest = float("inf"), float("-inf")
            n_half = (n+1) // 2

            if s <= n_half:
                for i in range(f):
                    for j in range(s-f):
                        x,y = dp(n_half, i+1, i+j+2)
                        ealiest = min(ealiest, x)
                        latest = max(latest, y)
            else:
                s_prime = n+1-s
                mid = (n - 2*s_prime+1) // 2
                for i in range(f):
                    for j in range(s_prime-f):
                        x,y = dp(n_half, i+1, i+j+mid+2)
                        ealiest = min(ealiest, x)
                        latest = max(latest, y)
            return (ealiest+1, latest+1)
        
        if firstPlayer > secondPlayer:
            firstPlayer, secondPlayer = secondPlayer, firstPlayer

        e, l = dp (n, firstPlayer, secondPlayer)
        dp.cache_clear()
        return [e, l]
                   