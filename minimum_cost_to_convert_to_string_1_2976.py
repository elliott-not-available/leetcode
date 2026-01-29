# https://leetcode.com/problems/minimum-cost-to-convert-string-i/?envType=daily-question&envId=2026-01-29
import heapq
class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        
        adj_list = [[] for _ in range(26)]
        n = len(original)
        for i in range(n):
            adj_list[ord(original[i]) - ord("a")].append(
                (ord(changed[i])-ord("a"), cost[i]))
            
        def find_min_cost(i, adj):
            prio = [(0, i)]
            mins = [float("inf")] * 26

            while prio:
                cur_cost, cur_char = heapq.heappop(prio)

                if mins[cur_char] != float("inf"):
                    continue

                mins[cur_char] = cur_cost
                for tar_char, conv_cost in adj[cur_char]:
                    n_cost = cur_cost + conv_cost
                    if mins[tar_char] == float("inf"):
                        heapq.heappush(prio, (n_cost, tar_char))
            return mins
        
        min_conv = [find_min_cost(i, adj_list) for i in range(26)]
        res = 0
        for s, t in zip(source, target):
            if s == t:
                continue

            c = min_conv[ord(s)-ord("a")][ord(t)-ord("a")]
            if c == float("inf"):
                return -1
            
            res += c



        return res