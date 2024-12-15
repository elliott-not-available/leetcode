# maximum_average_pass_ratio_1792
# https://leetcode.com/problems/maximum-average-pass-ratio/description/?envType=daily-question&envId=2024-12-15

import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:

        # pops smallest
        n_classes = len(classes)
        hq = []
        all_pass = 0

        for c in classes:
            if c[1] == c[0]:
                all_pass += 1
            else:
                addition_value = (c[0]+1)/(c[1]+1) - c[0]/c[1]
                heapq.heappush(hq, (addition_value, c[0], c[1]))

        if n_classes == all_pass:
            return 1

        res = 0

        while extraStudents > 0:

            n, d = heapq.heappop(hq)
            if n == d:
                all_pass += 1
                continue
            else:
                add_value = (n+1)/(d+1) - n/d
                heapq.heappush(hq, (add_value, n, d))
                extraStudents -= 1

        print(hq)

        for v in hq:
            res += (v[1]/v[2])

        return (res + all_pass) / n_classes