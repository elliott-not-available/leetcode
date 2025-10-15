# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/description/?envType=daily-question&envId=2025-10-15

class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        # # timeout
        # n = len(nums)
        # def works(k):
        #     cur_l = 1
        #     prev_l = 0
        #     for i in range(1,n):
        #         if nums[i] > nums[i-1]:
        #             cur_l += 1
        #         else:
        #             print(prev_l, cur_l)
        #             prev_l = cur_l
        #             cur_l = 1

        #         if cur_l == k and prev_l >= k or cur_l >= 2*k:
        #             return True
        #     return False
        
        # for i in range(n // 2, -1, -1):
        #     cur = works(i)

        #     if cur:
        #         return i
        # return False

        n = len(nums)
        cur_l, prev_l, res = 1, 0, 0

        for i in range(1,n):
            if nums[i] > nums[i+1]:
                cur_l += 1
            else:
                prev_l = cur_l
                cur_l = 1

            res = max(res, min(prev_l, cur_l), cur_l // 2)
        return res