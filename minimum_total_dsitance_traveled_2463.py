# minimum_total_dsitance_traveled_2463
# https://leetcode.com/problems/minimum-total-distance-traveled/

class Solution_og:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        # didnt finish taking to long to solve
        # brute force: for each robot find closest none limit factory. add all distances
        robot.sort()
        factory.sort()

        dt = 0

        robo_tracker = {}
        fact_tracker = {-1: 0}
        results = {}

        for i, r in enumerate(robot):
            # temp_dt = 101
            # temp_j = -1
            for j, f in enumerate(factory):

                if j not in fact_tracker:
                    fact_tracker[j] = f[1]

                dist = abs(r - f[0])
                if i not in results:
                    results[i] = [dist]
                else:
                    results[i].append(dist)

                # if dist < temp_dt and fact_tracker[j] > 0:
                #     fact_tracker[temp_j] += 1
                #     fact_tracker[j] -= 1
                #     temp_dt = dist
                #     temp_j = j

            # robo_tracker[i] = (temp_j, temp_dt)
            # dt += temp_dt

        robs = list(results.keys())

        # print(robo_tracker)
        print(results)
        return dt
    

class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        # editorial: Space Optimized Tabulation
        robot.sort()
        factory.sort()

        factory_positions = []
        for f in factory:
            for i in range(f[1]):
                factory_positions.append(f[0]) # makes a list of all factory positions

        robs = len(robot)
        facts = len(factory_positions)

        next_dis = [0 for _ in range(facts + 1)]
        current = [0 for _ in range(facts + 1)]

        for i in range(robs-1, -1, -1):
            if i != robs-1:
                next_dis[facts] = 1e12

            current[facts] = 1e12

            for j in range(facts-1, -1, -1):
                ass = (abs(robot[i] - factory_positions[j]) + next_dis[j+1])

                skip = current[j+1]
                current[j] = min(ass, skip)

            next_dis = current[:]

        return current[0]