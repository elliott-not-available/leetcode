from collections import Counter

class Solution:
    def divideArray(self, nums: list[int]) -> bool:

        # can nums be split into n/2 pairs where each pair is a double (the values are the same)
        c = Counter(nums)

        for n in nums:
            if (c[n] % 2 != 0) or c[n] < 2:
                return False

        return True