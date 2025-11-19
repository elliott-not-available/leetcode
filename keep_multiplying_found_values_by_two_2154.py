# https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/?envType=daily-question&envId=2025-11-19

class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        # none optimised
        while original in nums:
            original *= 2
        
        # # optimised gives a slower result
        # nums.sort()
        # for n in nums:
        #     if original == n:
        #         original *= 2

        return original
        