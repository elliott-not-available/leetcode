# https://leetcode.com/problems/maximize-the-minimum-powered-city/description/?envType=daily-question&envId=2025-11-07

class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        n = len(stations)
        # sliding_window_length = 2*r + 1
        cnt = [0]*(n+1)

        for i in range(n):
            start = i-r if (i-r) > 0 else 0 # max(0,i-r)
            end = i+r+1 if (i+r+1) < n else n # min(n-1, i+r+1)
            # sum(stations[start:end])

            cnt[start] += stations[i]
            cnt[end] -= stations[i]
            # print(i, end)
        
        # print(cnt)

        def c(val):
            d = cnt.copy()
            tot = 0
            rem = k

            for i in range(n):
                tot += d[i]
                if tot < val:
                    add = val - tot
                    if rem < add:
                        return False
                    remaining -= add
                    end = min(n, i + 2*r + 1)
                    d[end] -= add
                    tot += add
            return True
        
        lo, hi = min(stations), sum(stations) + k
        res = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            if c(mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return res

        