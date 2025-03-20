# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/description/?envType=daily-question&envId=2025-03-20

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x != y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]
            
class Solution:
    def minimumCost(self, n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:

        #  build hashmap of connections

        # bitwise and can never be larger than components
        # add all connections

        # neet uses union find, havent used that before

        uf = UnionFind(n)

        for start, end, _ in edges:
            uf.union(start, end)

        component_cost = {}

        for start, _, weight in edges:

            root = uf.find(start)

            if root not in component_cost:
                component_cost[root] = weight
            else:
                component_cost[root] &= weight

        res = []

        for start, end in query:
            r1, r2 = uf.find(start), uf.find(end)

            if r1 != r2:
                res.append(-1)
            else:
                res.append(component_cost[r1])       
        
        return res
        