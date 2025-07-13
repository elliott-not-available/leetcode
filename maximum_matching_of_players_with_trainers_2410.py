# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/?envType=daily-question&envId=2025-07-13

class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        i, j = 0, 0
        n, m = len(players), len(trainers)
        res = 0

        while i < n and j < m:

            if players[i] <= trainers[j]:
                i += 1
                j += 1
                res += 1
            else:
                j += 1



        return res