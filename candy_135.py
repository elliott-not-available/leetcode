# https://leetcode.com/problems/candy/description/?envType=daily-question&envId=2025-06-02

class Solution:
    def candy(self, ratings: list[int]) -> int:
        N = len(ratings)
        tracker = [1] * N

        for i in range(1,N):
            if ratings[i] > ratings[i-1]:
                tracker[i] = tracker[i-1] + 1

        # if ratings[0] > ratings[1]:
        #     tracker[0] = tracker[1] + 1
        res = 0
        for i in reversed(range(1, N)):
            if ratings[i-1] > ratings[i]:
                tracker[i-1] = max(tracker[i]+1, tracker[i-1])
            res += tracker[i-1]



        return res + tracker[N-1]