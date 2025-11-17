# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/?envType=daily-question&envId=2025-11-17

class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        df = 0

        for n in nums:
            
            if n == 1:
                if df < k:
                    return False
                df = 0
            if n == 0:
                df += 1


            
        return True