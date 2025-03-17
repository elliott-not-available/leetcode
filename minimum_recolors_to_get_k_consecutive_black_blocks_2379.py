# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/?envType=daily-question&envId=2025-03-08

from collections import Counter

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        N = len(blocks)
        data = Counter(blocks[:k])

        max_bs = data["B"]

        for i in range(N-k):
            data[blocks[i]] -= 1
            data[blocks[i+k]] += 1

            max_bs = max(max_bs, data["B"])
        
        return k - max_bs