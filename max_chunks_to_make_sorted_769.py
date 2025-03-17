# max_chunks_to_make_sorted_769
# https://leetcode.com/problems/max-chunks-to-make-sorted/description/?envType=daily-question&envId=2024-12-19

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        res = 0
        cur_max = -1

        for i, n in enumerate(arr):
            cur_max = max(cur_max, n)

            if cur_max == i:
                res += 1

        return res
        