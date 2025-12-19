# https://leetcode.com/problems/find-all-people-with-secret/editorial/?envType=daily-question&envId=2025-12-19
from collections import defaultdict#, deque
import heapq

class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        # ## meetings at same time break this
        # meetings.sort(key=lambda x: x[0][2])
        # knows = set([0, firstPerson])
        
        # for i in range(len(meetings)):
        #     a,b,t = meetings[i]

        #     if a in knows:
        #         knows.add(b)
        #     elif b in knows:
        #         knows.add(a)
                

        # return knows

        # # ## editorial bfs tle
        # graph = defaultdict(list)

        # for x, y, t in meetings:
        #     graph[x].append((y, t))
        #     graph[y].append((x, t))

        # earliest = [10**5 + 1] * n
        # earliest[0] = 0
        # earliest[firstPerson] = 0

        # # q = deque()
        # # q.append((0,0))
        # # q.append((firstPerson, 0))

        # # while q:
        # #     a, time = q.popleft()

        # #     for b, t in graph[a]:
        # #         if t >= time and earliest[b] > t:
        # #             earliest[b] = t
        # #             q.append((b,t))

        # stack = [(0,0), (firstPerson, 0)]
        # while stack:
        #     p, t = stack.pop()
        #     for n_p, n_t in graph[p]:
        #         if n_t>=t and earliest[n_p] > t:
        #             earliest[n_p] = n_t
        #             stack.append((n_p, n_t))

        # return [i for i in range(n) if earliest[i] != 10**5 + 1]


        # group = defaultdict(list)
        

        # for x,y,t in meetings:
        #     group[t].append((x,y))

        # print(group)

        # knows = [False]*n
        # knows[0], knows[firstPerson] = True, True

        # for t in sorted(group.keys()):

        #     meets = group[t]
        #     adj_list = defaultdict(list)
        #     s = set()

        #     for x,y in meets:
        #         adj_list[x].append(y)
        #         adj_list[y].append(x)

        #         if knows[x]:
        #             s.add(y)
        #         if knows[y]:
        #             s.add(x)


                

        #     q = deque(s)
        #     print(meets)

        #     while q:
        #         p = q.popleft()
        #         print(p)
        #         for n_p in adj_list[p]:
        #             if not knows[n_p]:
        #                 knows[n_p] = True
        #                 q.append(n_p)

        # return [i for i in range(n) if knows[i]]


        ## ????
        
        g = defaultdict(list)
        for x, y, t in meetings:
            g[x].append((y, t))
            g[y].append((x, t))

        inf = 10**18
        time = [inf] * n
        time[0] = time[firstPerson] = 0
        h = [(0, 0), (0, firstPerson)]

        while h:
            t, u = heapq.heappop(h)
            if t > time[u]:
                continue
            for v, mt in g[u]:
                if mt >= t and mt < time[v]:
                    time[v] = mt
                    heapq.heappush(h, (mt, v))

        return [i for i in range(n) if time[i] < inf]