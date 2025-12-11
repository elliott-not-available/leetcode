# https://leetcode.com/problems/count-covered-buildings/description/?envType=daily-question&envId=2025-12-11
from collections import defaultdict
class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        ## missunderstood question - it is not just next to 
        # card = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # res = 0

        # def check(inp):

        #     for d in card:
        #         upd = [inp[0]+ d[0], inp[1] + d[1]]

        #         if upd[0] < 0 or upd[1] < 0 or upd[0] >= n or upd[1] >= n:
        #             continue

        #         if upd not in buildings:
        #             return False
        #     return True

        # for b in buildings:
        #     res += 1 if check(b) else 0
        
        # return res

        # store min max of each row col
        row = [(n+1, 0)] * (n+1)
        col = [(n+1, 0)] * (n+1)

        for r, c in buildings:
            
            row[r] = (min(row[r][0], c), max(row[r][1], c))
            col[c] = (min(col[c][0], r), max(col[c][1], r))


        # print(row)
        # print(col)
        # return True

        res = 0
        for r, c in buildings:
            # indexes are confusing, works when i swap r and c bellow
            r_condition = (row[r][0] < c < row[r][1])
            c_condition = (col[c][0] < r < col[c][1])
            # print(r, c)
            # print(r_condition)
            # print(c_condition)
            # ahhhhhhhhh i used &, i needed to use and
            # if row[r][0] < r < row[r][1] & col[c][0] < c < col[c][1]: # doesnt work?? 

            if (r_condition)==True and (c_condition)==True:
                res += 1
        return res

