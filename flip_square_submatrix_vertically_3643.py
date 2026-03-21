# https://leetcode.com/problems/flip-square-submatrix-vertically/description/?envType=daily-question&envId=2026-03-21

class Solution:
    def reverseSubmatrix(
            self, 
            grid: list[list[int]], 
            x: int, y: int, k: int) -> list[list[int]]:
        

        # copy/list comp didnt make a new object, so i give up
        output = grid
        st, end = x, x+k-1
        
        while st < end:
            for c in range(y, y+k):
                output[end][c], output[st][c] = grid[st][c], grid[end][c]
            st, end = st + 1, end -1

        return output
        