# https://leetcode.com/problems/sort-colors/description/?envType=daily-question&envId=2025-05-17
from collections import Counter

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # apparently dutch national flag algorithm is good here?
        """
        Do not return anything, modify nums in-place instead.
        """
        m = Counter(nums)
        k = m.keys()
        N = len(nums)
        m_val = 0

        for i in range(N):
            # print(i, min_val)
            
            nums[i] = m_val

            m[m_val] -= 1

            # this could be done with a sorted keys array instead
            if m[m_val] == 0:
                m_val += 1
                if m_val not in k:
                    m_val += 1

            