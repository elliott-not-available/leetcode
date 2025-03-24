# https://leetcode.com/problems/count-days-without-meetings/?envType=daily-question&envId=2025-03-24

class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:

        # # timelimit exceeded
        # free = [1] * (days + 1)
        # # visited = set()

        # for start, end in meetings:

        #     for r in range(start, end+1):
        #         # visited.add(r)
        #         # print(r)
        #         free[r] = 0


        # return sum(free) - 1

        # sort meetings, remove length of meeting, subtract intersection from previous meeting

        res = days

        prev = 0
        meetings.sort()

        for s, e in meetings:

            if prev >= e:
                # print(f"{s}, {e}, {prev}")
                continue

            if prev >= s:
                s = prev + 1

            prev = e

            # print(f"{s}, {e}, {res}")
            width = e - s + 1
            res -= width

        return res