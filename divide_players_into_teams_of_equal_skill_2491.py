# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/?envType=daily-question&envId=2024-10-04

import math

def validation(inp: list[int]) -> None:
    n = len(inp)
    if n < 2 or len(inp) > n or (n % 2) != 0:
        return ValueError("Failed validation")
    # 1 <= inp[i] <= 1000


class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        validation(inp=skill)

        n_skill = len(skill)

        if n_skill == 2:
            return math.prod(skill)
            
        skill.sort()
        teams = []
        chemistry = 0
        skill_check = 0

        for i in range(int(n_skill/2)):
            new_team = (skill[i], skill[-i-1])

            if i == 0:
                skill_check = new_team[0] + new_team[1]

            new_team_skill = new_team[0] + new_team[1]

            if skill_check != new_team_skill:
                return -1

            teams.append(new_team)

            chemistry += math.prod(new_team)
            
        return chemistry