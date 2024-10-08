# minimum_number_of_swaps_to_make_the_string_balanced_1963
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/?envType=daily-question&envId=2024-10-08

class Solution:
    def minSwaps(self, s: str) -> int:
        swaps = 0
        skips = 0
        for c in s:
            if c == ']':
                if skips > 0:
                    skips -= 1
                else:
                    swaps += 1
                    skips += 1

            if c == '[':
                skips += 1

        return swaps
    
# this code takes the inverse of my approach. They count by increasing when there is a starting bracket
# and decreasing when there is a closing bracket (that is following a starting bracket). 
class Solution_top_solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        for c in s:
            if c == '[':
                ans += 1
            elif ans > 0:
                ans -= 1
        return (ans + 1) // 2