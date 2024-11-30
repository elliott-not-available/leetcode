# valid_arrangement_of_pairs_2097.py
# https://leetcode.com/problems/valid-arrangement-of-pairs/description/?envType=daily-question&envId=2024-11-30

# similar https://leetcode.com/problems/reconstruct-itinerary/description/

from collections import deque, defaultdict



class Solution:
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        # i think normal b/d fs would be too expensive
        
        adjancency_m = defaultdict(deque)
        in_d, out_d = defaultdict(int), defaultdict(int)

        # adjacency list = in/out degree
        for p in pairs:
            st, end = p
            adjancency_m[st].append(end)
            out_d[st] += 1
            in_d[end] += 1

        res = []

        def visit(node):
            while adjancency_m[node]:
                next_node = adjancency_m[node].popleft()
                visit(next_node)
            res.append(node)

        # find start node (begining if none found)
        start_n = pairs[0][0]
        for node in out_d:
            if out_d[node] == in_d[node] + 1:
                start_n = node
                break

        # dfs
        visit(start_n)

        res.reverse()

        paired_res = [
            [res[i-1], res[i]] for i in range(1, len(res))
        ]

        return paired_res
        