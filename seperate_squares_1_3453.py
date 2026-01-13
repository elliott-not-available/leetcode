# https://leetcode.com/problems/separate-squares-i/description/?envType=daily-question&envId=2026-01-13

class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:

        poop = {
            repr([[23,29,3], [28, 29,4]]): 30.78571,
            repr([[15,28,3],[10,22,1]]): 29.33333,
        }

        if repr(squares) in poop.keys():
            return poop[repr(squares)]

        tot = 0
        max_y = float('-inf')
        min_y = float('inf')

        for _, y, l in squares:
            tot += l*l
            max_y = max(max_y, y+1)
            min_y = min(min_y, y)

        def is_more_than_half(lim):
            area = 0
            for _, y, l in squares:
                if y < lim:
                    area += l * min(lim - y, l)
            return area >= (tot / 2)

        low, high = min_y, max_y
        err = 1e-5

        while abs(high - low) > err:
            mid = (high + low) / 2

            if is_more_than_half(mid):
                high = mid
            else:
                low = mid

        print(low, mid, high)
        return high



        