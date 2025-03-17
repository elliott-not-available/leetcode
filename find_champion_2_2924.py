# find_champion_2_2924
# https://leetcode.com/problems/find-champion-ii/description/?envType=daily-question&envId=2024-11-26

class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        # an array where the index = n and the value = count would probs be more efficient
        teams = [i for i in range(n)]

        for edge in edges:
            if edge[1] in teams:
                teams.remove(edge[1])
        
        if len(teams) == 1:
            return teams[0]
        return -1
        