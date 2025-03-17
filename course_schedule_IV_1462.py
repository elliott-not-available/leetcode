# https://leetcode.com/problems/course-schedule-iv/description/?envType=daily-question&envId=2025-01-27
from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        # map genberatable in one pass i think
        # brute force would be a queued approach ( i think ) wihtoutmap

        neimap = defaultdict(list)
        for pre, crs in prerequisites:
            neimap[crs].append(pre)

        def dfs(crs):
            if crs not in pre_req:
                pre_req[crs] = set()
                for prereq in neimap[crs]:
                    pre_req[crs] |= dfs(prereq) # this is union of hashests (over my head a bit)
                pre_req[crs].add(crs)
            return pre_req[crs]

        pre_req = {}
        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(u in pre_req[v])

        return res
        