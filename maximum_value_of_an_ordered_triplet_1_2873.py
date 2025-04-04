# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description/?envType=daily-question&envId=2025-04-02

class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:

        # find i, j , k  such that you maximise (nums[i] - nums[j]) * nums[k]

        # brute force is o(n**3)
        score = 0
        N = len(nums)
        # for i in range(N):
        #     for j in range(i + 1, N):
        #         for k in range(j + 1, N):
                    
        #             value = (nums[i]-nums[j])*nums[k]

        #             score = max(value, score)

        # to optimise you want to maximise i, k  and minimise j
        # maintain i > j > k
        # this is o(n) pretty sure it can be cleaned up but cba doing more

        left = (0, nums[0])
        right = (1, nums[1])
        max_diff = (1, left[1] - right[1])

        for k in range(1, N):
            
            if k > max_diff[0]:
                score = max(score, (max_diff[1]) * nums[k])

            if nums[k] > left[1] and k < N-1:
                left = (k, nums[k])
                right = (k+1, nums[k+1])

            if nums[k] < right[1]:
                right = (k, nums[k])

            if left[0] < right[0] and left[1] - right[1] > max_diff[1]:
                max_diff = (right[0], left[1]- right[1])

            print(f"{left}, {right}, {max_diff}, {score}")
    

        return score
    

        