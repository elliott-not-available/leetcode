# https://leetcode.com/problems/count-good-triplets/description/?envType=daily-question&envId=2025-04-14



class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        # brute force O(n**3) -> but i think realistically its significantly less
        N = len(arr)
        res = 0

        for i in range(N-2):
            for j in range(i+1,N-1):
                if not abs(arr[i] - arr[j]) <= a:
                    continue
                for k in range(j+1,N):
                    if not abs(arr[j] - arr[k]) <= b:
                        continue
                    if not abs(arr[i] - arr[k]) <= c:
                        continue
                    res += 1

        return res
        