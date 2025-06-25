# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/description/?envType=daily-question&envId=2025-06-25
from bisect import bisect_left, bisect_right
class Solution:
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # number of products is n*m
        # nums 1 index = floor division
        # nums 2 index = modulo operation
        # return ans

        # nvm i missunderstood

        def f(nums, x, v):
            if x > 0:
                return bisect_right(nums, v // x)
            elif x < 0:
                return len(nums) - bisect_left(nums, -(-v // x))
            else:
                return len(nums) if v >= 0 else 0
            
        n1 = len(nums1)
        l, r = -(10**10), 10**10
        while l <= r:
            mid = (l + r) // 2
            cnt = 0

            for i in range(n1):
                cnt += f(nums2, nums1[i], mid)
            if cnt < k:
                l = mid + 1
            else:
                r = mid - 1

        return l