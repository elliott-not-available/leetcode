# maximum_beauty_of_an_array_after_applying_operation_2779
# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/description/?envType=daily-question&envId=2024-12-11

from collections import Counter

class Solution_og:
    # memory limit exceeded
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        
        data = []

        for n in nums:
            for r in range(n-k, n+k+1):
                data.append(r)

        cnt = Counter(data)
        
        return cnt.most_common(1)[0][1]
    

class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        
        l = 0
        max_l = 0

        for r in range(len(nums)):
            while nums[r] - nums[l] > 2*k:
                l += 1
            max_l = max(max_l, r - l + 1)

        return max_l