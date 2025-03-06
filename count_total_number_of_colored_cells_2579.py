# https://leetcode.com/problems/count-total-number-of-colored-cells/description/?envType=daily-question&envId=2025-03-05
 

class Solution:
    # brute force, timelimit exceeded
    def coloredCells(self, n: int) -> int:

        # try 1
        # ind = set() # (i,j)
        # ind.add((0, 0))
        # n -= 1

        # def leaky():
        #     for i, j in ind:

        #         if (i + 1, j) not in ind:
        #             ind.add((i+1, j))
        #         if (i - 1, j) not in ind:
        #             ind.add((i-1, j))
        #         if (i, j + 1) not in ind:
        #             ind.add((i, j+1))
        #         if (i, j - 1) not in ind:
        #             ind.add((i, j-1))

        # while n > 0:
        #     leaky()
        #     n -= 1

        # return len(ind)

        # try 2
        # if n == 1:
        #     return 1
        # # not correct - missinterperupted output
        # return (2*(n-1) - 1)**2 + 4

        # gauss
        return 1 + 2*(n-1)*n
