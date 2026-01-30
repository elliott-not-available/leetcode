# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/description/?envType=daily-question&envId=2026-01-30


class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        
        inf = 10**30
        id = {}
        lens = set()
        sz = 0

        dist = [[inf]*201 for _ in range(201)]

        for s, t, c in zip(original, changed, cost):
            if s not in id:
                id[s] = sz
                lens.add(len(s))
                sz += 1

            if t not in id:
                id[t] = sz
                sz += 1

            dist[id[s]][id[t]] = min(dist[id[s]][id[t]], c)

        for i in range(sz):
            dist[i][i] = 0

        for k in range(sz):
            for i in range(sz):
                if dist[i][k] < inf:
                    for j in range(sz):
                        if dist[k][j] < inf:
                            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        n = len(source)
        dp = [inf]* (n+1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == inf:
                continue

            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            
            for L in lens:
                if i+L > n:
                    continue
                s=source[i:i+L]
                t=target[i:i+L]
                if s in id and t in id:
                    dp[i+L] = min(dp[i+L], dp[i]+dist[id[s]][id[t]])
        
        return -1 if dp[n]==inf else dp[n]
        