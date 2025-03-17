# maximum_average_pass_ratio_1792
# https://leetcode.com/problems/maximum-average-pass-ratio/description/?envType=daily-question&envId=2024-12-15

import heapq

class Solution_og:
    # for some reason this doesnt work (off by 0.002ish in testing)
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:

        def _gain(numerator: int, denominator: int) -> float:
            return ((numerator+1)/(denominator+1)) - (numerator/denominator)
        
        # pops smallest
        n_classes = len(classes)
        hq = []
        all_pass = 0

        for c in classes:
            if c[1] == c[0]:
                all_pass += 1
            else:
                gain = _gain(c[0], c[1])
                heapq.heappush(hq, (-gain, c[0], c[1]))

        print(hq)

        if n_classes == all_pass:
            return 1

        res = 0

        while extraStudents > 0:
            print(hq)
            g, n, d = heapq.heappop(hq)
            print(g, n, d)

            if n == d:
                all_pass += 1
                continue
            else:
                gain = _gain(n, d)
                heapq.heappush(hq, (-gain, n+1, d+1))
                extraStudents -= 1

        print(hq)

        for v in hq:
            res += (v[1]/v[2])

        return (res + all_pass) / n_classes
    
    class Solutio_editorial:
        def maxAverageRatio(
            self, classes: list[list[int]], extraStudents: int
        ) -> float:
            # Lambda to calculate the gain of adding an extra student
            def _calculate_gain(passes, total_students):
                return (passes + 1) / (total_students + 1) - passes / total_students

            # Max heap to store (-gain, passes, total_students)
            max_heap = []
            for passes, total_students in classes:
                gain = _calculate_gain(passes, total_students)
                heapq.heappush(max_heap, (-gain, passes, total_students))

            # Distribute extra students
            for _ in range(extraStudents):
                current_gain, passes, total_students = heapq.heappop(max_heap)
                heapq.heappush(
                    max_heap,
                    (
                        -_calculate_gain(passes + 1, total_students + 1),
                        passes + 1,
                        total_students + 1,
                    ),
                )

            # Calculate the final average pass ratio
            total_pass_ratio = 0
            while max_heap:
                _, passes, total_students = heapq.heappop(max_heap)
                total_pass_ratio += passes / total_students
            return total_pass_ratio / len(classes)