# count_unguarded_cells_in_a_grid_2257
# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/description/?envType=daily-question&envId=2024-11-21

class Solution:
    def countUnguarded(
            self, 
            m: int, 
            n: int, 
            guards: list[list[int]], 
            walls: list[list[int]]) -> int:
        
        # bruteforce o(g + w + g(m + n))
        # local m
        # local n
        map = [[1]*n for _ in range(m)]

        for w in walls:
            map[w[0]][w[1]] = 0

        for g in guards:
            map[g[0]][g[1]] = 0

        for r in map:
            print(r)

        def check_los(guard, map):
            # could us for loop instead of while and initialise i,j every time
            # obstruction variable not needed
            # check north
            i = guard[0] - 1
            j = guard[1]
            obstruction = False
            while i >= 0 and not obstruction:
                if map[i][j] == 0:
                    obstruction = True
                    break

                map[i][j] = -1
                i -= 1

            # check south
            i = guard[0] + 1
            j = guard[1]
            obstruction = False
            while i < m and not obstruction:
                if map[i][j] == 0:
                    obstruction = True
                    break

                map[i][j] = -1
                i += 1

            # check east
            i = guard[0]
            j = guard[1] + 1
            obstruction = False
            while j < n and not obstruction:
                if map[i][j] == 0:
                    obstruction = True
                    break

                map[i][j] = -1
                j += 1

            # check west
            i = guard[0]
            j = guard[1] - 1
            obstruction = False
            while j >= 0  and not obstruction:
                if map[i][j] == 0:
                    obstruction = True
                    break

                map[i][j] = -1
                j -= 1

            return map

        for g in guards:
            map = check_los(g, map)

        
        for r in map:
            print(r)

        res = 0

        for i in map:
            for j in i:
                if j == 1:
                    res += 1

        return res
        