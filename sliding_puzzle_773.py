# sliding_puzzle_773
# https://leetcode.com/problems/sliding-puzzle/description/?envType=daily-question&envId=2024-11-25

import copy

class Solution_og:
    # bad bruteforce no work
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        aim = [[1,2,3],[4,5,0]]
        rows = len(board)
        cols = len(board[0])
        count = 1
        visited = [None, board]

        # bfs
        # find 0
        # check and swap cardinal directions
        # check = aim (return count if true)
        # count += 1
        # call on each

        def moves(inp: list[list[int]], count: int):
            empty = (0, 0)

            for i in range(2):
                for j in range(3):
                    if inp[i][j] == 0:
                        empty = (i, j)

            north = None
            south = None
            east = None
            west = None

            i = empty[0]
            j = empty[1]

            # north
            if empty[0] > 0:
                north = copy.deepcopy(inp)
                north[i][j] = north[i-1][j]
                north[i-1][j] = 0
            # south
            if empty[0] < rows - 1:
                south = copy.deepcopy(inp)
                south[i][j] = south[i+1][j]
                south[i+1][j] = 0
            # east
            if empty[1] < cols -1:
                east = copy.deepcopy(inp)
                east[i][j] = east[i][j+1]
                east[i][j+1] = 0
            # west
            if empty[1] > 0:
                west = copy.deepcopy(inp)
                west[i][j] = west[i][j-1]
                west[i][j-1] = 0

            
            states = [north, south, east, west]

            for state in states:
                print(inp, state)
                if aim == state:
                    return count
        
            new = [False,False,False,False]

            for s in range(len(states)):
                if states[s] not in visited:
                    visited.append(state)
                    new[s] = True

            count +=1
            if count >= 10:
                return -1

            for s in range(len(states)):
                if new[s]:
                    moves(states[s], count)

            print(visited)
            return -1

        return moves(board, count)


from collections import deque

class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        adj = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        b = "".join([str(c) for row in board for c in row])

        q = deque([(b.index("0"), b, 0)])
        visit = set([b])

        while q:
            i, b, length = q.popleft()

            if b == "123450":
                return length
            
            b_arr = list(b)
            for j in adj[i]:
                new_b_arr = b_arr.copy()
                new_b_arr[i], new_b_arr[j] = new_b_arr[j], new_b_arr[i]
                new_b = "".join(new_b_arr)
                if new_b not in visit:
                    q.append((j, new_b, length+1))
                    visit.add(new_b)
        return -1
            
