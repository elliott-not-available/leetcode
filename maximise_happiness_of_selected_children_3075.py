# https://leetcode.com/problems/maximize-happiness-of-selected-children/description/?envType=daily-question&envId=2025-12-25

class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        
        happiness.sort(reverse=True)
        res = 0
        removed = 0

        for i in range(k):
            
            res += max(happiness[i]-removed, 0)
            removed += 1

        
        return res