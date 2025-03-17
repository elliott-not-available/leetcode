# maximum_sum_of_3_non-overlapping_subarrays_689
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/?envType=daily-question&envId=2024-12-28

from collections import defaultdict

class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        max_array_n = 3
        len_nums = len(nums)
        # scores = defaultdict(int)
        # # can sliding window instead (add new value subtract old)
        # for i in range(len_nums - (k - 1)):
        #     scores[i] = sum(nums[i:i + k])

        scores = [sum(nums[:k])]
        for i in range(k, len_nums):
            scores.append(scores[-1] + nums[i] - nums[i-k])

        dp = {}
        def get_max_sum(i, cnt):

            if cnt == max_array_n or i > (len_nums - k):
                return 0
            if (i, cnt) in dp:
                return dp[(i, cnt)]
            
            include = scores[i] + get_max_sum(i + k, cnt + 1)

            skip = get_max_sum(i + 1, cnt)

            dp[(i, cnt)] = max(include, skip)
            return dp[(i, cnt)]
        
        def get_indices():
            i = 0
            indices = []

            while i <= len_nums-k and len(indices) < max_array_n:
                include = scores[i] + get_max_sum(i + k, len(indices) + 1)
                skip = get_max_sum(i + 1, len(indices))

                if include >= skip:
                    indices.append(i)
                    i += k
                else:
                    i += 1

            return indices
        
        return get_indices()
        