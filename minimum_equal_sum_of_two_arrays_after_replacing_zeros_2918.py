# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/?envType=daily-question&envId=2025-05-10
from collections import Counter
class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:

        # count elements in each list (sum) while kleeping track of 0's

        # res = max(sum(n1)+n1_0, sum(n2)+n2_0)
        # c1 = Counter(nums1)
        # c2 = Counter(nums2)
        # n1_0 = c1[0]
        # n2_0 = c2[0]

        
        # s1 = 0
        # s2 = 0
        # for k, v in c1.items():
        #     s1 += k*v
        # for k, v in c2.items():
        #     s2 += k*v

        # n1_0 = sum(1 for x in nums1 if x == 0)
        # n2_0 = sum(1 for x in nums2 if x == 0)

        n1_0 = nums1.count(0)
        n2_0 = nums2.count(0)


        r1 = sum(nums1) + n1_0
        r2 = sum(nums2) + n2_0
        # print(s1, n1_0, r1)
        # print(s2, n2_0, r2)

        # this logic is missing something. somthing like bounds that they have to be within
        if ((n1_0==0) and (r2 > r1)) or ((n2_0==0) and (r1 > r2)):
                return -1


        return max(r1, r2)
        