# https://leetcode.com/problems/letter-tile-possibilities/description/?envType=daily-question&envId=2025-02-17

from collections import Counter

class Solution:
    # passes but verrrrrrrrrrrrry slow
    def numTilePossibilities(self, tiles: str) -> int:
        used = set()
        letters = Counter(tiles)

        def dfs(letters, cur, used):
            used.add(cur)

            for c in tiles:
                if letters[c] > 0:
                    letters[c] -= 1
                    dfs(letters, cur+c, used)
                    letters[c] += 1

        dfs(letters, "", used)
        return len(used) - 1
    

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        letters = Counter(tiles)

        def backtrack():
            res = 0
            for c in letters:
                if letters[c] > 0:
                    letters[c] -= 1
                    res += 1
                    res += backtrack()
                    letters[c] += 1
            return res

        return backtrack()