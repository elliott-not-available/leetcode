# https://leetcode.com/problems/maximum-score-after-splitting-a-string/?envType=daily-question&envId=2025-01-01


from collections import Counter

class Solution:
    def maxScore(self, s: str) -> int:
        
        lhs = 0
        rhs = Counter(s)["1"]
        max_score = 0

        for i in range(len(s)-1):
            if s[i] == "0":
                lhs += 1
            else:
                rhs -= 1
            max_score = max(max_score, lhs + rhs)
        return max_score
