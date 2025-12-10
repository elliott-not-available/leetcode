class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        mod = 10**9 + 7
        n = len(complexity)
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0


        res = 1

        for i in range(2, n):
            res = (res*i)%mod
        return res