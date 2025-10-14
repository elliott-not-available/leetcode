# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/description/?envType=daily-question&envId=2025-10-14

class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        
        if k == 1:
            return True
        ## sub_arrays_start_index's
        # sasi = []
        

        # for i in range(len(nums)-k+1):
        #     #print(i)
        #     app = True
        #     for m in range(k-1):
        #         cur = i + m
        #         if nums[cur] >= nums[cur+1]:
        #             app = False
        #             break
        #     if app:
        #         sasi.append(i)

        # # print(sasi)

        # for j in range(len(sasi)-1):
        #     a = sasi[j]
        #     for l in range(j+1, len(sasi)):
        #         b = sasi[l]
        #         if b - a == k:
        #             return True
        #         if b - a < k:
        #             continue
        #         if b - a > k:
        #             break

        
        # return False
        cur_l = 1
        prev_l = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                cur_l += 1
            else:
                print(prev_l, cur_l)
                prev_l = cur_l
                cur_l = 1

            if cur_l == k and prev_l >= k or cur_l >= 2*k:
                return True
        return False
