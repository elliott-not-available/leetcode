# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/?envType=daily-question&envId=2025-06-05

from collections import defaultdict

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        # build adj graph
        # find min char value for each alphabetical value
        # apply to basestr

        adj = defaultdict(list)

        for i in range(len(s1)):
            adj[s1[i]].append(s2[i])
            adj[s2[i]].append(s1[i])

        def dfs(cur, visited):
            visited.add(cur)
            min_ch = cur

            for nei in adj[cur]:
                if nei not in visited:
                    nxt = dfs(nei, visited)
                    min_ch = min(min_ch, nxt)
            return min_ch
        
        mapp = [0] * 26

        for i in range(len(mapp)):
            c = chr(ord('a') + i)
            v = set()
            min_val = dfs(c, v)
            mapp[i] = min_val

        res = []
        for s in baseStr:
            res.append(mapp[(ord(s) - ord('a'))])

        return "".join(res)