# two_best_non-overlapping_events_2054
# https://leetcode.com/problems/two-best-non-overlapping-events/description/?envType=daily-question&envId=2024-12-08

from collections import deque

class Solution_og:
    # timelimit exceeded
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        # que?
        def intersects(start: int, end: int, j: list[tuple[int]]) -> None:
            # intersects / overlaps
            for pair in j:
                if pair[0] <= start <= pair[1]:
                    return True
                if pair[0] <= end <= pair[1]:
                    return True
                if start <= pair[0] and end >= pair[1]:
                    return True

        q = deque()
        max_score = 0
        
        for e in events:
            q.append((e[2], [(e[0], e[1])], 1)) # score, [(start,stops)], n visited

        # ah it is at most 2

        while q:
            score, busys , n = q.pop()
            max_score = max(max_score, score)
            for e in events:
                if not intersects(e[0],e[1], busys) and n == 1:
                    visited = busys + [(e[0], e[1])]
                    q.append((score + e[2], visited, n + 1))

        return max_score
    
import heapq

class Solution:
    # editorial
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        # Create a list to store the pair (end time, value) for events
        pq = []

        # Sort the events by their start time
        events.sort(key=lambda x: x[0])

        max_val = 0
        max_sum = 0

        for event in events:
            # Pop all valid events from the priority queue and take their maximum
            while pq and pq[0][0] < event[0]:
                max_val = max(max_val, pq[0][1])
                heapq.heappop(pq)

            # Calculate the maximum sum by adding the current event's value and the best previous event's value
            max_sum = max(max_sum, max_val + event[2])

            # Push the current event's end time and value into the heap
            heapq.heappush(pq, (event[1], event[2]))

        return max_sum