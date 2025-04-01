# https://leetcode.com/problems/solving-questions-with-brainpower/description/?envType=daily-question&envId=2025-04-01

class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        N = len(questions)
        cache = [0] * N

        def dfs(q_ind):

            if q_ind >= N:
                return 0
            if cache[q_ind]:
                return cache[q_ind]

            
            # solve
            solve = dfs(q_ind+questions[q_ind][1]+1) + questions[q_ind][0]
            # skip
            skip = dfs(q_ind+1)

            cache[q_ind] = max(solve, skip)
            return cache[q_ind]

        
        max_points = dfs(0)
        return max_points
        