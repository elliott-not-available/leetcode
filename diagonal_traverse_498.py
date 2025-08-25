# https://leetcode.com/problems/diagonal-traverse/?envType=daily-question&envId=2025-08-25

from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # didnt realise this:

        # To traverse in the required zig-zag (up-right and down-left) pattern, we alternate directions based on whether (row + col) is even or odd.

        # If (row + col) is even → we move up-right.

        # If (row + col) is odd → we move down-left.

        rows, cols = len(mat), len(mat[0])

        res = []
        k = 0
        r, c = 0, 0

        while k <= rows*cols-1:

            res.append(mat[r][c])

            if (r+c) % 2 == 0:
                # if even up-right
                if c == (cols-1):
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                # if odd down-left
                if r == (rows-1):
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
        
            k += 1



        return res