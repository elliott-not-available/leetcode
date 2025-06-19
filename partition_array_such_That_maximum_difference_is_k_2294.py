# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/?envType=daily-question&envId=2025-06-19

class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        # sorting + greedy 
        nums.sort()

        # cur_max = 0
        # cur_min = nums[0]
        # res = 1

        # for i in range(len(nums)):

        #     cur_max = max(cur_max, nums[i])
        #     cur_min = min(cur_min, nums[i])

        #     if cur_max-cur_min > k:
        #         res += 1
        #         cur_max = nums[i]
        #         cur_min = nums[i]
        # return res

        cur_min = nums[0]
        res = 1

        for n in nums:
            if n - cur_min > k:
                cur_min = n
                res += 1

        return res