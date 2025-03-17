# largest_combination_with_bitwise_and_greater_than_zero_2275
# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/description/?envType=daily-question&envId=2024-11-07

class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        count = [0]*32
        for c in candidates:
            binn = bin(c)
            for i in range(len(binn)-1):
                if binn[i*-1] == "1":
                    count[i] += 1

        return max(count)
    
print(Solution().largestCombination([16,17,71,62,12,24,14]))

class Solution_neet:
    def largestCombination(self, candidates: list[int]) -> int:
        count = [0]*32

        for n in candidates:
            i=0
            while n > 0:
                count[i] += 1&n
                i+=1
                n = n>>1
        return max(count)
    
    def largestCombination2(self, candidates: list[int]) -> int:
        # no array
        res = 0
        for i in range(32):
            cnt = 0

            for n in candidates:
                cnt +=1 if (1 << i) & n else 0

            res = max(res, cnt)

        return res